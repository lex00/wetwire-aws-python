#!/usr/bin/env python3
"""AWS SAM samples import script for wetwire-aws.

This script tests wetwire-aws's import functionality against official
AWS SAM templates from various repositories.

Workflow:
1. Clone SAM template repositories to temp directory
2. Find all SAM templates (templates with AWS::Serverless resources)
3. Import templates in parallel
4. Validate generated packages
5. Report statistics

Usage:
  python scripts/import_sam_samples.py                     # Full import with validation
  python scripts/import_sam_samples.py --clean             # Clean output before running
  python scripts/import_sam_samples.py --skip-validation   # Skip package validation
  python scripts/import_sam_samples.py --verbose           # Show detailed progress
"""

import argparse
import multiprocessing
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Literal

# SAM template repositories to fetch
SAM_REPOS = [
    {
        "name": "aws-sam-cli-app-templates",
        "url": "https://github.com/aws/aws-sam-cli-app-templates.git",
        "description": "Official SAM CLI init templates",
    },
    {
        "name": "sessions-with-aws-sam",
        "url": "https://github.com/aws-samples/sessions-with-aws-sam.git",
        "description": "Real-world SAM examples from Twitch series",
    },
]

# Templates to exclude from import (non-standard, macros, etc.)
EXCLUDE_PATTERNS = [
    # Jinja templates (need preprocessing)
    "cookiecutter",
    ".jinja",
    ".j2",
    # Node modules
    "node_modules",
    # Test fixtures
    "__tests__",
    "test-",
    # Build artifacts
    ".aws-sam",
    "dist/",
    "build/",
    # Templates referencing implicit SAM resources (auto-generated roles, stages)
    "sam-containers-demo-app",
    "api-enhanced-observability-variables",
    "go-al2",
    "safe-deploy",
    "lambda-layers/demo-app",
    "custom-domains/both-implied",
    "custom-domains/both-declared",
]

# Templates with known defects that should be skipped during validation
SKIP_VALIDATION = [
    # Templates referencing implicit API stages in depends_on
    "sessions_with_aws_sam_multi_level_mapping_admin",
    "sessions_with_aws_sam_multi_level_mapping_reportin",
    "sessions_with_aws_sam_multi_level_mapping_dadjokes",
]

# Colors for output
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
NC = "\033[0m"  # No Color


def info(msg: str) -> None:
    """Print info message."""
    print(f"{BLUE}==>{NC} {msg}")


def success(msg: str) -> None:
    """Print success message."""
    print(f"{GREEN}✓{NC} {msg}")


def warn(msg: str) -> None:
    """Print warning message."""
    print(f"{YELLOW}⚠{NC} {msg}")


def error(msg: str) -> None:
    """Print error message."""
    print(f"{RED}✗{NC} {msg}")


def header(msg: str) -> None:
    """Print section header."""
    print()
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{CYAN}  {msg}{NC}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print()


def is_sam_template(template_path: Path) -> bool:
    """Check if a template is a SAM template."""
    try:
        content = template_path.read_text()
        # Check for SAM Transform or SAM resource types
        if "AWS::Serverless" in content:
            return True
        if "Transform:" in content and "Serverless" in content:
            return True
        return False
    except Exception:
        return False


def should_exclude(template_path: Path) -> bool:
    """Check if a template should be excluded."""
    path_str = str(template_path).lower()
    for pattern in EXCLUDE_PATTERNS:
        if pattern.lower() in path_str:
            return True
    return False


def import_template(
    template: Path, output_dir: Path, project_root: Path, verbose: bool
) -> tuple[Literal["OK", "FAIL", "SKIP"], str, str]:
    """Import a single SAM template.

    Returns:
        Tuple of (status, package_name, error_output)
    """
    template_name = template.name
    stem = template.stem
    # Create unique package name from path
    rel_path = template.relative_to(template.parent.parent.parent)
    path_parts = list(rel_path.parent.parts) + [stem]
    pkg_name = "_".join(re.sub(r"[^a-zA-Z0-9_]", "_", p).lower() for p in path_parts)
    pkg_name = re.sub(r"_+", "_", pkg_name).strip("_")[:50]  # Limit length
    pkg_output = output_dir / pkg_name

    # Remove existing to ensure fresh import
    if pkg_output.exists():
        shutil.rmtree(pkg_output)

    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "wetwire-aws",
                "import",
                str(template),
                "-o",
                str(pkg_output),
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            # Check if it's because no resources were found
            if "No resources found" in result.stderr:
                return ("SKIP", pkg_name, "")
            error_output = f"=== {template} ===\n{result.stderr}\n"
            return ("FAIL", pkg_name, error_output)

        if verbose:
            print(f"  Imported: {template_name} -> {pkg_name}", file=sys.stderr)
        return ("OK", pkg_name, "")
    except subprocess.TimeoutExpired:
        return ("FAIL", pkg_name, f"=== {template} ===\nTimeout after 30s\n")
    except subprocess.CalledProcessError as e:
        error_output = f"=== {template} ===\n{e.stderr}\n"
        return ("FAIL", pkg_name, error_output)


def validate_package(
    pkg_dir: Path, project_src: Path, project_root: Path
) -> tuple[Literal["OK", "FAIL"], str, str]:
    """Validate a single package by importing it.

    Returns:
        Tuple of (status, package_name, error_output)
    """
    outer_name = pkg_dir.name

    # Find the actual package name (inner directory)
    inner_pkg = None
    for d in pkg_dir.iterdir():
        if d.is_dir() and (d / "__init__.py").exists():
            inner_pkg = d.name
            break

    if not inner_pkg:
        error_output = f"=== {outer_name} ===\nNo __init__.py found in package\n"
        return ("FAIL", outer_name, error_output)

    # Validate by importing the package
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{project_src}:{pkg_dir}"

    try:
        subprocess.run(
            ["uv", "run", "python", "-c", f"import {inner_pkg}"],
            cwd=project_root,
            env=env,
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return ("OK", outer_name, "")
    except subprocess.TimeoutExpired:
        return (
            "FAIL",
            outer_name,
            f"=== {outer_name} ===\nTimeout during validation\n",
        )
    except subprocess.CalledProcessError as e:
        error_output = f"=== {outer_name} ({inner_pkg}) ===\n{e.stderr}\n"
        return ("FAIL", outer_name, error_output)


def clone_repo(repo: dict, clone_dir: Path) -> bool:
    """Clone a repository."""
    repo_name = repo["name"]
    repo_url = repo["url"]
    target_dir = clone_dir / repo_name

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(target_dir)],
            capture_output=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Import SAM templates from official AWS repositories"
    )
    parser.add_argument(
        "--clean", action="store_true", help="Clean examples directory before running"
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip running each package to validate it works",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed progress"
    )
    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    output_dir = project_root / "examples" / "aws-sam-templates"

    # Check if uv is installed
    if not shutil.which("uv"):
        error("uv is not installed. Please install uv first:")
        print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
        return 1

    # Check if git is installed
    if not shutil.which("git"):
        error("git is not installed")
        return 1

    # Number of parallel jobs
    jobs = min(multiprocessing.cpu_count(), 8)

    # Step 1: Optionally clean output directory
    if args.clean and output_dir.exists():
        header("Cleaning Output Directory")
        shutil.rmtree(output_dir)
        success(f"Removed existing {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 2: Clone SAM repositories
    temp_dir = Path(tempfile.mkdtemp())
    header("Cloning SAM Template Repositories")
    info(f"Temp directory: {temp_dir}")

    cloned_repos = []
    for repo in SAM_REPOS:
        info(f"Cloning {repo['name']} ({repo['description']})...")
        if clone_repo(repo, temp_dir):
            success(f"Cloned {repo['name']}")
            cloned_repos.append(temp_dir / repo["name"])
        else:
            warn(f"Failed to clone {repo['name']}")

    if not cloned_repos:
        error("Failed to clone any repositories")
        shutil.rmtree(temp_dir)
        return 1

    try:
        # Step 3: Find all SAM templates
        header("Discovering SAM Templates")

        templates = []
        for repo_dir in cloned_repos:
            for ext in ["*.yaml", "*.yml", "*.json"]:
                for template in repo_dir.rglob(ext):
                    if should_exclude(template):
                        continue
                    if is_sam_template(template):
                        templates.append(template)

        total_templates = len(templates)
        info(f"Found {total_templates} SAM templates to import")

        if total_templates == 0:
            error("No SAM templates found in repositories")
            return 1

        # Step 4: Import templates in parallel
        header(f"Importing SAM Templates ({jobs} parallel jobs)")

        import_errors_file = output_dir / "import_errors.log"
        import_errors_file.write_text("")

        import_ok = 0
        import_fail = 0
        import_skip = 0
        import_errors = []

        with ProcessPoolExecutor(max_workers=jobs) as executor:
            futures = {
                executor.submit(
                    import_template, template, output_dir, project_root, args.verbose
                ): template
                for template in templates
            }

            for future in as_completed(futures):
                status, pkg_name, error_output = future.result()
                if status == "OK":
                    import_ok += 1
                elif status == "SKIP":
                    import_skip += 1
                else:
                    import_fail += 1
                    import_errors.append(error_output)

        if import_errors:
            with open(import_errors_file, "w") as f:
                f.write("\n".join(import_errors))

        success(f"Imported: {import_ok}  Skipped: {import_skip}  Failed: {import_fail}")

        # Step 5: Lint packages to fix forward references
        header("Linting Packages")

        lint_errors_file = output_dir / "lint_errors.log"
        try:
            subprocess.run(
                ["uv", "run", "wetwire-aws", "lint", "--fix", str(output_dir)],
                cwd=project_root,
                capture_output=True,
                text=True,
                check=True,
            )
            success("Linted all packages")
        except subprocess.CalledProcessError as e:
            lint_errors_file.write_text(e.stderr)
            warn(f"Some lint issues could not be fixed (see {lint_errors_file})")

        # Step 6: Validate packages
        validation_failed = []

        if not args.skip_validation:
            header(f"Validating Packages ({jobs} parallel jobs)")

            package_dirs = [d for d in output_dir.iterdir() if d.is_dir()]
            total_packages = len(package_dirs)

            if total_packages == 0:
                warn("No packages to validate")
            else:
                validation_errors_file = output_dir / "validation_errors.log"
                validation_errors_file.write_text("")

                validated_count = 0
                validation_errors = []
                project_src = project_root / "src"

                # Filter out packages in SKIP_VALIDATION
                packages_to_validate = []
                for pkg_dir in package_dirs:
                    if pkg_dir.name in SKIP_VALIDATION:
                        warn(f"{pkg_dir.name} (skipped - known implicit resource refs)")
                    else:
                        packages_to_validate.append(pkg_dir)

                with ProcessPoolExecutor(max_workers=jobs) as executor:
                    futures = {
                        executor.submit(
                            validate_package, pkg_dir, project_src, project_root
                        ): pkg_dir
                        for pkg_dir in packages_to_validate
                    }

                    for future in as_completed(futures):
                        status, pkg_name, error_output = future.result()
                        if status == "OK":
                            if args.verbose:
                                success(pkg_name)
                            validated_count += 1
                        else:
                            error(pkg_name)
                            validation_failed.append(pkg_name)
                            validation_errors.append(error_output)

                if validation_errors:
                    with open(validation_errors_file, "w") as f:
                        f.write("\n".join(validation_errors))

                success(f"Validated: {validated_count}/{total_packages} packages")
        else:
            warn("Skipping validation (--skip-validation flag)")

        # Step 7: Report
        header("Summary")

        print()
        success(f"Total SAM templates found: {total_templates}")
        success(f"Successful imports: {import_ok}")
        if import_skip > 0:
            info(f"Skipped (no resources): {import_skip}")
        if import_fail > 0:
            warn(f"Failed imports: {import_fail}")
        if validation_failed:
            warn(f"Failed validation: {len(validation_failed)}")
        print()

        info(f"Output directory: {output_dir}")
        if import_errors_file.exists() and import_errors_file.stat().st_size > 0:
            info(f"Import errors: {import_errors_file}")
        validation_errors_file = output_dir / "validation_errors.log"
        if (
            validation_errors_file.exists()
            and validation_errors_file.stat().st_size > 0
        ):
            info(f"Validation errors: {validation_errors_file}")
        print()

        # Exit with appropriate code
        if validation_failed:
            warn(
                "Completed with validation failures - examples preserved for inspection"
            )
            return 1
        else:
            success("All SAM templates imported successfully!")
            return 0

    finally:
        # Cleanup temp directory
        if temp_dir.exists():
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    sys.exit(main())
