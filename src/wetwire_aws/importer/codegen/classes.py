"""Class generation functions for CloudFormation elements.

This module generates Python dataclass definitions for CloudFormation
template elements.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from wetwire_aws.importer.ir import (
    IRCondition,
    IRMapping,
    IROutput,
    IRParameter,
    IRResource,
)

from .blocks import property_value_to_python_block
from .context import AnnotatedValue
from .helpers import (
    PARAMETER_TYPE_MAP,
    resolve_resource_type,
    sanitize_class_name,
)
from .values import (
    escape_docstring,
    escape_string,
    value_to_python,
)

if TYPE_CHECKING:
    from .context import CodegenContext


# =============================================================================
# Parameter Class Generation
# =============================================================================


def generate_parameter_class(param: IRParameter, ctx: CodegenContext) -> str:
    """Generate a Parameter class using inheritance pattern."""
    lines = []

    # Docstring
    if ctx.include_docstrings and param.description:
        lines.append(f"    {escape_docstring(param.description)}")
        lines.append("")

    # Import Parameter base class
    ctx.add_import("wetwire_aws", "Parameter")

    # Type - use constant if available
    if param.type in PARAMETER_TYPE_MAP:
        const_name = PARAMETER_TYPE_MAP[param.type]
        ctx.add_import("wetwire_aws", const_name)
        lines.append(f"    type = {const_name}")
    else:
        lines.append(f"    type = {escape_string(param.type)}")

    # Optional fields
    if param.description:
        lines.append(f"    description = {escape_string(param.description)}")
    if param.default is not None:
        lines.append(f"    default = {value_to_python(param.default, ctx)}")
    if param.allowed_values:
        lines.append(
            f"    allowed_values = {value_to_python(param.allowed_values, ctx)}"
        )
    if param.allowed_pattern:
        lines.append(f"    allowed_pattern = {escape_string(param.allowed_pattern)}")
    if param.min_length is not None:
        lines.append(f"    min_length = {param.min_length}")
    if param.max_length is not None:
        lines.append(f"    max_length = {param.max_length}")
    if param.min_value is not None:
        lines.append(f"    min_value = {param.min_value}")
    if param.max_value is not None:
        lines.append(f"    max_value = {param.max_value}")
    if param.constraint_description:
        lines.append(
            f"    constraint_description = {escape_string(param.constraint_description)}"
        )
    if param.no_echo:
        lines.append("    no_echo = True")

    class_name = sanitize_class_name(param.logical_id)
    # Use inheritance pattern: class MyParam(Parameter):
    return f"class {class_name}(Parameter):\n" + "\n".join(lines)


# =============================================================================
# Resource Class Generation
# =============================================================================


def generate_resource_class(resource: IRResource, ctx: CodegenContext) -> str:
    """Generate a resource wrapper class using inheritance pattern."""
    ctx.current_resource_id = resource.logical_id
    lines = []

    # Resolve resource type
    resolved = resolve_resource_type(resource.resource_type)

    # Build class declaration with inheritance
    wrapper_class_name = sanitize_class_name(resource.logical_id)

    if resolved:
        module, type_class_name = resolved
        ctx.current_module = module

        # Import the module for inheritance: class MyBucket(s3.Bucket)
        ctx.add_import("wetwire_aws.resources", module)
        class_decl = f"class {wrapper_class_name}({module}.{type_class_name}):"
    else:
        # Unknown resource type - use base class
        ctx.add_import("wetwire_aws.base", "CloudFormationResource")
        class_decl = f"class {wrapper_class_name}(CloudFormationResource):"
        lines.append(f"    # Unknown resource type: {resource.resource_type}")

    # Properties - use block mode for all values
    for prop in resource.properties.values():
        # Get expected type from PropertyType info if available
        expected_type = None  # TODO: Look up from resource spec

        # Use block mode to generate wrapper classes for nested structures
        value_result = property_value_to_python_block(
            prop.value,
            resource.logical_id,
            prop.python_name,
            expected_type,
            module if resolved else None,
            ctx,
        )

        if isinstance(value_result, AnnotatedValue):
            lines.append(
                f"    {prop.python_name}: {value_result.annotation} = {value_result.value}"
            )
        else:
            lines.append(f"    {prop.python_name} = {value_result}")

    # Resource-level attributes
    if resource.depends_on:
        dep_strs = []
        has_implicit = False
        for dep in resource.depends_on:
            if dep in ctx.template.resources:
                # Known resource - use bare class name
                dep_strs.append(sanitize_class_name(dep))
            else:
                # Unknown resource - likely SAM implicit, use string
                dep_strs.append(f'"{dep}"')
                has_implicit = True
        comment = "  # SAM implicit resource" if has_implicit else ""
        lines.append(f"    depends_on = [{', '.join(dep_strs)}]{comment}")
    if resource.condition:
        lines.append(f"    condition = {escape_string(resource.condition)}")
    if resource.deletion_policy:
        lines.append(f"    deletion_policy = {escape_string(resource.deletion_policy)}")

    # Add 'pass' if no body to avoid syntax error
    if not lines:
        lines.append("    pass")

    return f"{class_decl}\n" + "\n".join(lines)


# =============================================================================
# Output Class Generation
# =============================================================================


def generate_output_class(output: IROutput, ctx: CodegenContext) -> str:
    """Generate an Output class using inheritance pattern."""
    lines = []

    # Docstring
    if ctx.include_docstrings and output.description:
        lines.append(f"    {escape_docstring(output.description)}")
        lines.append("")

    ctx.add_import("wetwire_aws", "Output")

    # Value
    value_str = value_to_python(output.value, ctx, indent=1)
    lines.append(f"    value = {value_str}")

    # Optional fields
    if output.description:
        lines.append(f"    description = {escape_string(output.description)}")
    if output.export_name:
        export_str = value_to_python(output.export_name, ctx, indent=1)
        lines.append(f"    export_name = {export_str}")
    if output.condition:
        lines.append(f"    condition = {escape_string(output.condition)}")

    class_name = sanitize_class_name(output.logical_id)
    # Use inheritance pattern: class MyOutput(Output):
    return f"class {class_name}Output(Output):\n" + "\n".join(lines)


# =============================================================================
# Mapping Class Generation
# =============================================================================


def generate_mapping_class(mapping: IRMapping, ctx: CodegenContext) -> str:
    """Generate a Mapping class using inheritance pattern."""
    lines = []

    ctx.add_import("wetwire_aws", "Mapping")

    # Map data as dict
    map_str = value_to_python(mapping.map_data, ctx, indent=1)
    lines.append(f"    map_data = {map_str}")

    class_name = sanitize_class_name(mapping.logical_id)
    # Use inheritance pattern: class MyMapping(Mapping):
    return f"class {class_name}Mapping(Mapping):\n" + "\n".join(lines)


# =============================================================================
# Condition Class Generation
# =============================================================================


def generate_condition_class(condition: IRCondition, ctx: CodegenContext) -> str:
    """Generate a Condition class using inheritance pattern."""
    lines = []

    ctx.add_import("wetwire_aws", "Condition as TemplateCondition")

    # Store the original logical ID for CloudFormation serialization
    lines.append(f"    logical_id = {escape_string(condition.logical_id)}")

    # Expression
    expr_str = value_to_python(condition.expression, ctx, indent=1)
    lines.append(f"    expression = {expr_str}")

    class_name = sanitize_class_name(condition.logical_id)
    # Use inheritance pattern: class MyCondition(TemplateCondition):
    return f"class {class_name}Condition(TemplateCondition):\n" + "\n".join(lines)
