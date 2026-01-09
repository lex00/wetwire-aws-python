"""Shared fixtures for lint rule tests."""

from unittest.mock import patch

import pytest

from wetwire_aws.linter.rules import StringShouldBeEnum


@pytest.fixture
def mock_enum_available():
    """Mock _is_enum_available to always return True for testing.

    This allows testing enum detection logic without requiring actual
    enum generation (which needs botocore).
    """
    with patch.object(StringShouldBeEnum, "_is_enum_available", return_value=True):
        yield
