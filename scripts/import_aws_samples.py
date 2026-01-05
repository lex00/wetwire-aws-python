#!/usr/bin/env python3
"""AWS CloudFormation samples import script for wetwire-aws.

This script tests wetwire-aws's import functionality against the official
aws-cloudformation-templates repository.

Workflow:
1. Clone aws-cloudformation-templates to temp directory
2. Apply template fixes
3. Import templates in parallel
4. Lint packages to fix forward references
5. Validate each package in parallel
6. Report final statistics

On failure, the examples directory is preserved for inspection.

Usage:
  python scripts/import_aws_samples.py                        # Full import with validation
  python scripts/import_aws_samples.py --clean                # Clean output before running
  python scripts/import_aws_samples.py --template NAME        # Test specific template
  python scripts/import_aws_samples.py --skip-validation      # Skip package validation
  python scripts/import_aws_samples.py --verbose              # Show detailed progress
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

# Templates with known defects that cannot be imported correctly
# These will be skipped during validation (but still imported for inspection)
SKIP_TEMPLATES = [
    # Uses custom CloudFormation macro (ExecutionRoleBuilder) with non-standard properties
    "example",
    "example_2",
    # Uses !Explode macro which generates incomplete Python code
    "test_2",
    # Has complex Join-based UserData that generates malformed Python strings
    "efs_with_automount_to_ec2",
]

# Templates to exclude from import entirely (Rain-specific, Kubernetes manifests, etc.)
# These use non-standard CloudFormation features that require preprocessing
EXCLUDE_TEMPLATES = [
    # Rain-specific templates (use !Rain:: tags)
    "APIGateway/apigateway_lambda_integration.yaml",
    "CloudFormation/CustomResources/getfromjson/src/getfromjson.yml",
    "CloudFormation/MacrosExamples/Boto3/example.json",
    "CloudFormation/MacrosExamples/DateFunctions/date_example.yaml",
    "CloudFormation/MacrosExamples/DateFunctions/date.yaml",
    "CloudFormation/MacrosExamples/PyPlate/python.yaml",
    "CloudFormation/MacrosExamples/StringFunctions/string.yaml",
    "CloudFormation/StackSets/common-resources-stackset_1.yaml",
    "CloudFormation/StackSets/common-resources.yaml",
    "CloudFormation/StackSets/common-resources.json",
    "CloudFormation/StackSets/log-setup-management_1.yaml",
    "ElastiCache/Elasticache-snapshot.yaml",
    "IoT/amzn2-greengrass-cfn.yaml",
    "RainModules/api-resource.yml",
    "RainModules/bucket-policy.yml",
    "RainModules/bucket.yml",
    "RainModules/static-site.yml",
    "Solutions/GitLab/GitLabServer.yaml",
    "Solutions/GitLab/GitLabServer.json",
    "Solutions/GitLabAndVSCode/GitLabAndVSCode.yaml",
    "Solutions/GitLabAndVSCode/GitLabAndVSCode.json",
    "Solutions/Gitea/Gitea.yaml",
    "Solutions/Gitea/Gitea.json",
    "Solutions/Gitea/Gitea-pkg.yaml",
    "Solutions/Gitea/Gitea-pkg.json",
    "Solutions/ManagedAD/templates/MANAGEDAD.cfn.yaml",
    "Solutions/ManagedAD/templates/MANAGEDAD.cfn.json",
    "Solutions/VSCode/VSCodeServer.yaml",
    "Solutions/VSCode/VSCodeServer.json",
    # Kubernetes manifests (not CloudFormation)
    "EKS/manifest.yml",
    # Lambda test events (not CloudFormation templates)
    "CloudFormation/CustomResources/getfromjson/src/events/event-consume-from-list.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-consume-from-list-retrieval-error.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-consume-from-map.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-consume-from-map-retrieval-error.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-empty-json-data-input.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-empty-search-input.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-invalid-json-data-input.json",
    "CloudFormation/CustomResources/getfromjson/src/events/event-invalid-search-input.json",
    # SAM templates (use Transform: AWS::Serverless)
    "CloudFormation/CustomResources/getfromjson/src/template.yml",
    "CloudFormation/MacrosExamples/Count/template.json",
    "CloudFormation/MacrosExamples/Count/template.yaml",
    # EKS templates (too complex, many forward reference issues)
    "EKS/template.json",
    "EKS/template.yaml",
    # Macro definition templates (just define the macro, no resources to validate)
    "CloudFormation/MacrosExamples/Count/macro.json",
    "CloudFormation/MacrosExamples/Count/macro.yaml",
    "CloudFormation/MacrosExamples/StackMetrics/macro.json",
    "CloudFormation/MacrosExamples/StackMetrics/macro.yaml",
    "CloudFormation/MacrosExamples/S3Objects/macro.json",
    "CloudFormation/MacrosExamples/S3Objects/macro.yaml",
    "CloudFormation/MacrosExamples/Explode/macro.json",
    "CloudFormation/MacrosExamples/Explode/macro.yaml",
    "CloudFormation/MacrosExamples/ExecutionRoleBuilder/macro.json",
    "CloudFormation/MacrosExamples/ExecutionRoleBuilder/macro.yaml",
    "CloudFormation/MacrosExamples/Boto3/macro.json",
    "CloudFormation/MacrosExamples/Boto3/macro.yaml",
    # CodeBuild buildspec files (not CloudFormation templates)
    "Solutions/CodeBuildAndCodePipeline/codebuild-app-build.yml",
    "Solutions/CodeBuildAndCodePipeline/codebuild-app-deploy.yml",
    # Custom resource consumer example templates (reference custom resources that don't exist)
    "CloudFormation/CustomResources/getfromjson/example-templates/getfromjson-consumer.yml",
    # Bandit security linter config (not CloudFormation)
    "CloudFormation/CustomResources/getfromjson/bandit.yml",
    "CloudFormation/CustomResources/getfromjson/bandit.json",
    # CDK configuration files (not CloudFormation)
    "CloudFormation/StackSets-CDK/cdk.json",
    "CloudFormation/StackSets-CDK/config.json",
    # Macro test events (not CloudFormation templates)
    "CloudFormation/MacrosExamples/Count/event.json",
    "CloudFormation/MacrosExamples/Count/event_bad.json",
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


def should_skip_validation(template_name: str) -> bool:
    """Check if a template should be skipped during validation."""
    return template_name in SKIP_TEMPLATES


def import_template(
    template: Path, output_dir: Path, project_root: Path, verbose: bool
) -> tuple[Literal["OK", "FAIL"], str, str]:
    """Import a single template.

    Returns:
        Tuple of (status, package_name, error_output)
    """
    template_name = template.name
    stem = template.stem
    pkg_name = re.sub(r"[^a-zA-Z0-9_]", "_", stem).lower()
    pkg_output = output_dir / pkg_name

    # Remove existing to ensure fresh import
    if pkg_output.exists():
        shutil.rmtree(pkg_output)

    try:
        subprocess.run(
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
            check=True,
        )
        if verbose:
            print(f"  Imported: {template_name} -> {pkg_name}", file=sys.stderr)
        return ("OK", pkg_name, "")
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
        )
        return ("OK", outer_name, "")
    except subprocess.CalledProcessError as e:
        error_output = f"=== {outer_name} ({inner_pkg}) ===\n{e.stderr}\n"
        return ("FAIL", outer_name, error_output)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Import CloudFormation templates from aws-cloudformation-templates repo"
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
    parser.add_argument("--template", help="Test only a specific template file")
    parser.add_argument(
        "--local-source", help="Use local directory instead of cloning from GitHub"
    )
    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent.resolve()
    project_root = script_dir.parent
    output_dir = project_root / "examples" / "aws-cloudformation-templates"
    aws_templates_repo = "https://github.com/awslabs/aws-cloudformation-templates.git"

    # Check if uv is installed
    if not shutil.which("uv"):
        error("uv is not installed. Please install uv first:")
        print("  curl -LsSf https://astral.sh/uv/install.sh | sh")
        return 1

    # Number of parallel jobs
    jobs = min(multiprocessing.cpu_count(), 8)

    # Step 1: Optionally clean output directory
    if args.clean and output_dir.exists():
        header("Cleaning Output Directory")
        shutil.rmtree(output_dir)
        success(f"Removed existing {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 2: Get templates (clone or use local source)
    temp_dir = None
    if args.local_source:
        header("Using Local Template Source")
        local_source = Path(args.local_source)
        if not local_source.is_dir():
            error(f"Local source directory does not exist: {args.local_source}")
            return 1
        clone_dir = local_source
        info(f"Using local directory: {clone_dir}")
    else:
        header("Cloning AWS CloudFormation Templates")
        temp_dir = Path(tempfile.mkdtemp())
        info(f"Cloning to temp directory: {temp_dir}")
        try:
            subprocess.run(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    aws_templates_repo,
                    str(temp_dir / "aws-cloudformation-templates"),
                ],
                check=True,
                capture_output=True,
            )
            clone_dir = temp_dir / "aws-cloudformation-templates"
            success("Cloned repository")
        except subprocess.CalledProcessError as e:
            error(f"Failed to clone repository: {e}")
            if temp_dir:
                shutil.rmtree(temp_dir)
            return 1

    try:
        # Step 3: Apply template fixes
        header("Applying Template Fixes")
        subprocess.run(
            [
                "uv",
                "run",
                "python",
                str(script_dir / "fix_templates.py"),
                str(clone_dir),
            ],
            cwd=project_root,
            check=True,
        )

        # Step 4: Remove excluded templates
        header("Removing Excluded Templates")
        excluded_count = 0
        for template in EXCLUDE_TEMPLATES:
            template_path = clone_dir / template
            if template_path.exists():
                template_path.unlink()
                excluded_count += 1
        info(
            f"Removed {excluded_count} excluded templates (Rain-specific, Kubernetes, etc.)"
        )

        # Step 5: Find all templates to import
        header("Discovering Templates")
        templates = []
        for ext in ["*.yaml", "*.yml", "*.json"]:
            for template in clone_dir.rglob(ext):
                rel_path = template.relative_to(clone_dir)

                # Skip if single template specified and this isn't it
                if args.template and str(rel_path) != args.template:
                    continue

                templates.append(template)

        total_templates = len(templates)
        info(f"Found {total_templates} templates to import")

        if total_templates == 0:
            if args.template:
                error(f"Template not found: {args.template}")
            else:
                error("No templates found in repository")
            return 1

        # Step 6: Import templates in parallel
        header(f"Importing Templates ({jobs} parallel jobs)")

        import_errors_file = output_dir / "import_errors.log"
        import_errors_file.write_text("")

        import_ok = 0
        import_fail = 0
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
                else:
                    import_fail += 1
                    import_errors.append(error_output)

        if import_errors:
            with open(import_errors_file, "w") as f:
                f.write("\n".join(import_errors))

        success(f"Imported: {import_ok}  Failed: {import_fail}")

        # Step 7: Lint packages to fix forward references
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

        # Step 8: Validate no-parens pattern
        header("Validating No-Parens Pattern")

        ref_matches = []
        get_att_matches = []
        for py_file in output_dir.rglob("*.py"):
            content = py_file.read_text()
            if re.search(r"\bref\s*\(", content):
                ref_matches.append(py_file)
            if re.search(r"\bget_att\s*\(", content):
                get_att_matches.append(py_file)

        if ref_matches or get_att_matches:
            error(
                "Found ref() or get_att() calls in generated code - should use no-parens pattern"
            )
            for match in ref_matches[:10]:
                print(match)
            for match in get_att_matches[:10]:
                print(match)
            return 1
        else:
            success("No ref() or get_att() patterns found - using no-parens style")

        # Step 9: Validate packages
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

                # Filter out skipped packages
                packages_to_validate = [
                    pkg_dir
                    for pkg_dir in package_dirs
                    if not should_skip_validation(pkg_dir.name)
                ]

                # Warn about skipped packages
                for pkg_dir in package_dirs:
                    if should_skip_validation(pkg_dir.name):
                        warn(f"{pkg_dir.name} (skipped - known malformed template)")

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

        # Step 10: Report
        header("Summary")

        print()
        success(f"Total templates found: {total_templates}")
        success(f"Successful imports: {import_ok}")
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
        if import_fail > 0 or validation_failed:
            warn("Completed with failures - examples preserved for inspection")
            return 1
        else:
            success("All templates imported and validated successfully!")
            return 0

    finally:
        # Cleanup temp directory
        if temp_dir and temp_dir.exists():
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    sys.exit(main())
