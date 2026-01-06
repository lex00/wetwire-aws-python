#!/usr/bin/env python3
"""
Generate the serverless resource package from SAM spec.

This script generates typed dataclasses for AWS SAM resources in
src/wetwire_aws/resources/serverless/.

Usage:
    uv run python scripts/generate_serverless.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

# Add parent directory to path for codegen imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from codegen.config import RESOURCES_DIR
from codegen.extract_enums import get_sam_enums
from codegen.generate import generate_service_package
from codegen.parse import parse_sam_resources


def main():
    """Generate the serverless package."""
    print("Generating serverless package from SAM spec...")
    print("=" * 50)

    # Parse SAM resources
    print("\nParsing SAM resources...")
    schema = parse_sam_resources()

    # Filter to serverless service
    resources = [r for r in schema.resources if r.service == "serverless"]
    nested = [n for n in schema.nested_types if n.service == "serverless"]

    print(f"  Found {len(resources)} resources")
    print(f"  Found {len(nested)} property types")

    # Get SAM enums
    print("\nLoading SAM enums...")
    sam_enums = get_sam_enums()
    enum_count = len(sam_enums)
    print(f"  Found {enum_count} enums")

    # Convert enum format for generate_service_package
    service_enums = [(name, data) for name, data in sam_enums.items()]

    # Generate package files
    print("\nGenerating files...")
    files = generate_service_package(
        service="serverless",
        resources=resources,
        nested_types=nested,
        cf_spec_version="SAM-2016-10-31",
        service_enums=service_enums,
    )

    print(f"  Generated {len(files)} files")

    # Create package directory
    package_dir = RESOURCES_DIR / "serverless"
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)

    # Write files
    print("\nWriting files...")
    for filename, content in files.items():
        filepath = RESOURCES_DIR / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content + "\n")
        print(f"  {filename}")

    # Format with ruff
    if shutil.which("ruff"):
        print("\nFormatting with ruff...")
        result = subprocess.run(
            ["ruff", "format", str(package_dir), "--quiet"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"  Formatted {len(files)} files")
        else:
            print(f"  Warning: ruff formatting failed: {result.stderr}")

    print("\n" + "=" * 50)
    print("Serverless package generated successfully!")
    print(f"Output: {package_dir}")


if __name__ == "__main__":
    main()
