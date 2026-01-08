"""Kiro CLI integration for wetwire-aws.

This module provides integration with Kiro CLI for AI-assisted
infrastructure design using the wetwire-aws toolchain.

Usage:
    from wetwire_aws.kiro import install_kiro_configs, launch_kiro

    # Install configurations (first run)
    install_kiro_configs()

    # Launch Kiro with wetwire-runner agent
    launch_kiro(prompt="Create an S3 bucket with versioning")
"""

from wetwire_aws.kiro.installer import (
    check_kiro_installed,
    install_kiro_configs,
    launch_kiro,
    run_kiro_scenario,
)

__all__ = [
    "check_kiro_installed",
    "install_kiro_configs",
    "launch_kiro",
    "run_kiro_scenario",
]
