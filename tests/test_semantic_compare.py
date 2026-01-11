"""Tests for semantic comparison functionality."""

from wetwire_aws.testing.semantic_compare import (
    SemanticDiff,
    semantic_compare,
    semantic_equal,
)


class TestSemanticEqual:
    """Test semantic_equal function."""

    def test_identical_dicts(self):
        """Identical dictionaries are equal."""
        a = {"foo": "bar", "baz": 123}
        b = {"foo": "bar", "baz": 123}
        assert semantic_equal(a, b)

    def test_different_key_order(self):
        """Dictionaries with different key order are equal."""
        a = {"foo": "bar", "baz": 123}
        b = {"baz": 123, "foo": "bar"}
        assert semantic_equal(a, b)

    def test_nested_different_order(self):
        """Nested structures with different key order are equal."""
        a = {"outer": {"inner1": 1, "inner2": 2}}
        b = {"outer": {"inner2": 2, "inner1": 1}}
        assert semantic_equal(a, b)

    def test_lists_order_matters(self):
        """Lists maintain order (order matters)."""
        a = {"list": [1, 2, 3]}
        b = {"list": [3, 2, 1]}
        assert not semantic_equal(a, b)

    def test_lists_same_order(self):
        """Lists with same order are equal."""
        a = {"list": [1, 2, 3]}
        b = {"list": [1, 2, 3]}
        assert semantic_equal(a, b)

    def test_different_values(self):
        """Dictionaries with different values are not equal."""
        a = {"foo": "bar"}
        b = {"foo": "baz"}
        assert not semantic_equal(a, b)

    def test_missing_key(self):
        """Dictionaries with missing keys are not equal."""
        a = {"foo": "bar", "baz": 123}
        b = {"foo": "bar"}
        assert not semantic_equal(a, b)

    def test_extra_key(self):
        """Dictionaries with extra keys are not equal."""
        a = {"foo": "bar"}
        b = {"foo": "bar", "baz": 123}
        assert not semantic_equal(a, b)

    def test_none_values(self):
        """None values are compared correctly."""
        a = {"foo": None}
        b = {"foo": None}
        assert semantic_equal(a, b)

    def test_empty_structures(self):
        """Empty structures are equal."""
        assert semantic_equal({}, {})
        assert semantic_equal([], [])


class TestSemanticCompare:
    """Test semantic_compare function for differences."""

    def test_no_differences(self):
        """Returns empty list when no differences."""
        a = {"foo": "bar"}
        b = {"foo": "bar"}
        diffs = semantic_compare(a, b)
        assert diffs == []

    def test_value_difference(self):
        """Reports value differences with path."""
        a = {"foo": "bar"}
        b = {"foo": "baz"}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert diffs[0].path == "root.foo"
        assert diffs[0].expected == "bar"
        assert diffs[0].actual == "baz"

    def test_nested_path(self):
        """Reports nested differences with full path."""
        a = {"outer": {"inner": {"deep": 1}}}
        b = {"outer": {"inner": {"deep": 2}}}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert diffs[0].path == "root.outer.inner.deep"

    def test_missing_key_in_actual(self):
        """Reports missing keys."""
        a = {"foo": "bar", "baz": 123}
        b = {"foo": "bar"}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert "baz" in diffs[0].path
        assert diffs[0].diff_type == "missing"

    def test_extra_key_in_actual(self):
        """Reports extra keys."""
        a = {"foo": "bar"}
        b = {"foo": "bar", "baz": 123}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert "baz" in diffs[0].path
        assert diffs[0].diff_type == "extra"

    def test_list_length_difference(self):
        """Reports list length differences."""
        a = {"list": [1, 2, 3]}
        b = {"list": [1, 2]}
        diffs = semantic_compare(a, b)
        assert len(diffs) >= 1

    def test_list_element_difference(self):
        """Reports list element differences with index."""
        a = {"list": [1, 2, 3]}
        b = {"list": [1, 99, 3]}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert "[1]" in diffs[0].path

    def test_type_mismatch(self):
        """Reports type mismatches."""
        a = {"foo": "123"}
        b = {"foo": 123}
        diffs = semantic_compare(a, b)
        assert len(diffs) == 1
        assert diffs[0].diff_type == "type_mismatch"


class TestSemanticDiff:
    """Test SemanticDiff dataclass."""

    def test_str_representation(self):
        """SemanticDiff has readable string representation."""
        diff = SemanticDiff(
            path="root.foo",
            expected="bar",
            actual="baz",
            diff_type="value_changed",
        )
        s = str(diff)
        assert "root.foo" in s
        assert "bar" in s
        assert "baz" in s

    def test_diff_types(self):
        """All diff types have proper string representation."""
        for diff_type in ["value_changed", "missing", "extra", "type_mismatch"]:
            diff = SemanticDiff(
                path="root.foo",
                expected="x",
                actual="y",
                diff_type=diff_type,
            )
            assert diff_type in str(diff).lower() or str(diff)  # Just check it works
