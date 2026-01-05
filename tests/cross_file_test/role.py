"""Role resource defined in a separate file."""

from . import *  # noqa: F401, F403, F405

__all__ = ["AppRole"]


class AppRole(iam.Role):  # noqa: F405
    """IAM role for the application."""

    role_name = "app-role"
    assume_role_policy_document: dict = None
