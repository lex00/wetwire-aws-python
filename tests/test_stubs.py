"""Tests for stub generation configuration."""

import wetwire_aws
from wetwire_aws.stubs import AWS_CORE_EXPORTS


class TestStubConfig:
    """Tests for AWS_STUB_CONFIG."""

    def test_stub_exports_exist_in_wetwire_aws(self):
        """All symbols in AWS_CORE_EXPORTS must exist in wetwire_aws.__all__."""
        actual_exports = set(wetwire_aws.__all__)
        stub_exports = set(AWS_CORE_EXPORTS)

        missing = stub_exports - actual_exports
        assert not missing, (
            f"Symbols in AWS_CORE_EXPORTS but not in wetwire_aws.__all__: {sorted(missing)}"
        )
