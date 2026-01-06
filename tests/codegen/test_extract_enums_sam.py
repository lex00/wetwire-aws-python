"""Tests for SAM enum extraction in codegen/extract_enums.py."""

from codegen.extract_enums import (
    CF_TO_BOTOCORE_SERVICE,
    extract_enums_for_services,
    get_botocore_service,
    get_sam_enums,
)


class TestServerlessEnumMapping:
    """Tests for serverless service mapping."""

    def test_serverless_in_mapping(self):
        """Serverless should be in CF_TO_BOTOCORE_SERVICE."""
        assert "serverless" in CF_TO_BOTOCORE_SERVICE

    def test_serverless_maps_to_none(self):
        """Serverless should map to None (no botocore equivalent)."""
        assert CF_TO_BOTOCORE_SERVICE["serverless"] is None

    def test_get_botocore_service_returns_none_for_serverless(self):
        """get_botocore_service should return None for serverless."""
        result = get_botocore_service("serverless")
        assert result is None


class TestExtractEnumsForServerless:
    """Tests for extracting enums for serverless service."""

    def test_handles_serverless_gracefully(self):
        """extract_enums_for_services should not crash for serverless."""
        result = extract_enums_for_services(["serverless"])
        # Should return empty dict or SAM enums, not crash
        assert isinstance(result, dict)


class TestGetSAMEnums:
    """Tests for get_sam_enums function."""

    def test_returns_dict(self):
        """get_sam_enums should return a dict."""
        result = get_sam_enums()
        assert isinstance(result, dict)

    def test_has_runtime_enum(self):
        """Should include Runtime enum."""
        result = get_sam_enums()
        assert "Runtime" in result

    def test_runtime_has_python_values(self):
        """Runtime enum should include Python runtimes."""
        result = get_sam_enums()
        runtime = result["Runtime"]
        values = [v["value"] for v in runtime["values"]]
        assert "python3.12" in values
        assert "python3.11" in values

    def test_runtime_has_node_values(self):
        """Runtime enum should include Node.js runtimes."""
        result = get_sam_enums()
        runtime = result["Runtime"]
        values = [v["value"] for v in runtime["values"]]
        assert "nodejs20.x" in values

    def test_has_architecture_enum(self):
        """Should include Architecture enum."""
        result = get_sam_enums()
        assert "Architecture" in result

    def test_architecture_has_values(self):
        """Architecture enum should have x86_64 and arm64."""
        result = get_sam_enums()
        arch = result["Architecture"]
        values = [v["value"] for v in arch["values"]]
        assert "x86_64" in values
        assert "arm64" in values

    def test_has_package_type_enum(self):
        """Should include PackageType enum."""
        result = get_sam_enums()
        assert "PackageType" in result

    def test_package_type_has_values(self):
        """PackageType enum should have Zip and Image."""
        result = get_sam_enums()
        pkg_type = result["PackageType"]
        values = [v["value"] for v in pkg_type["values"]]
        assert "Zip" in values
        assert "Image" in values

    def test_enum_values_have_python_names(self):
        """Enum values should have Python-safe names."""
        result = get_sam_enums()
        runtime = result["Runtime"]
        for v in runtime["values"]:
            assert "name" in v
            assert "value" in v
            # Python name should be uppercase with underscores
            assert v["name"].isupper() or v["name"].startswith("_")
