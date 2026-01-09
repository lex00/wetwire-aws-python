"""Style-related lint rules.

Rules:
    WAW011: Use no-parens style for PropertyType wrappers
    WAW013: Use wrapper classes instead of inline constructors
    WAW014: Use wrapper classes instead of inline policy documents
    WAW015: Use wrapper classes instead of inline security group rules
    WAW016: Use wrapper classes instead of inline policy statements
    WAW017: Use wrapper class instead of inline property type dict
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class PropertyTypeAsRef(LintRule):
    """Detect PropertyType wrapper instantiation that should use no-parens style.

    PropertyType wrapper classes should be referenced as bare class names, not
    instantiated with `()`. The serialization layer auto-instantiates these.

    This follows the no-parens declarative pattern where all wiring is expressed
    as class references rather than instance construction.

    Detects:
    - field = MyPropertyTypeWrapper()  (with empty parens)
    - statement = [AllowStatement()]  (with empty parens in list)

    Suggests:
    - field = MyPropertyTypeWrapper
    - statement = [AllowStatement]
    """

    rule_id = "WAW011"
    description = "Use no-parens style for PropertyType wrappers"

    # Known PropertyType base classes from wetwire_aws
    PROPERTY_TYPE_BASES = {
        "PolicyDocument",
        "PolicyStatement",
        "DenyStatement",
        "Tag",
        "PropertyType",
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # First pass: identify PropertyType wrapper classes in this file
        # A PropertyType wrapper has a `resource:` annotation pointing to a PropertyType
        property_type_wrappers: set[str] = set()

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ClassDef):
                # Check for resource: annotation in class body
                for stmt in node.body:
                    if isinstance(stmt, ast.AnnAssign):
                        target = stmt.target
                        if isinstance(target, ast.Name) and target.id == "resource":
                            # Check what the annotation points to
                            if self._is_property_type_annotation(stmt.annotation):
                                property_type_wrappers.add(node.name)
                                break

        if not property_type_wrappers:
            return issues

        # Second pass: find usages of these wrappers with ()
        for node in ast.walk(context.tree):
            # Check direct assignments: field = WrapperClass()
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        # Skip if target is 'resource' (the type annotation field)
                        if target.id == "resource":
                            continue

                        value = node.value
                        # Check for Call with no args: field = WrapperClass()
                        if isinstance(value, ast.Call):
                            if (
                                isinstance(value.func, ast.Name)
                                and value.func.id in property_type_wrappers
                                and not value.args
                                and not value.keywords
                            ):
                                original = ast.get_source_segment(context.source, value)
                                if original:
                                    class_name = value.func.id
                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use no-parens style: {class_name}",
                                            line=value.lineno,
                                            column=value.col_offset,
                                            original=original,
                                            suggestion=class_name,
                                            fix_imports=[],
                                        )
                                    )

                        # Check lists: field = [WrapperClass(), WrapperClass2()]
                        elif isinstance(value, ast.List):
                            for elt in value.elts:
                                if isinstance(elt, ast.Call):
                                    if (
                                        isinstance(elt.func, ast.Name)
                                        and elt.func.id in property_type_wrappers
                                        and not elt.args
                                        and not elt.keywords
                                    ):
                                        original = ast.get_source_segment(
                                            context.source, elt
                                        )
                                        if original:
                                            class_name = elt.func.id
                                            issues.append(
                                                LintIssue(
                                                    rule_id=self.rule_id,
                                                    message=f"Use no-parens style: {class_name}",
                                                    line=elt.lineno,
                                                    column=elt.col_offset,
                                                    original=original,
                                                    suggestion=class_name,
                                                    fix_imports=[],
                                                )
                                            )

        return issues

    def _is_property_type_annotation(self, annotation: ast.expr) -> bool:
        """Check if an annotation refers to a PropertyType.

        Returns True for:
        - Name nodes like PolicyDocument, PolicyStatement, DenyStatement
        - Attribute nodes like s3.Bucket.SomePropertyType (nested in a module)
        """
        if isinstance(annotation, ast.Name):
            return annotation.id in self.PROPERTY_TYPE_BASES

        if isinstance(annotation, ast.Attribute):
            # Check for nested property types like s3.Bucket.BucketEncryption
            # or rds.DBProxy.TagFormat
            # These have at least one nested module (not just s3.Bucket which is a Resource)
            parts = self._get_attribute_parts(annotation)
            if len(parts) >= 3:
                # Format: module.Resource.PropertyType (e.g., s3.Bucket.BucketEncryption)
                # This is a nested PropertyType
                return True
            if len(parts) >= 2:
                # Check if the class name is in our known PropertyType bases
                class_name = parts[-1]
                return class_name in self.PROPERTY_TYPE_BASES

        return False

    def _get_attribute_parts(self, node: ast.expr) -> list[str]:
        """Extract parts from a nested Attribute node.

        For s3.Bucket.BucketEncryption, returns ['s3', 'Bucket', 'BucketEncryption'].
        """
        parts: list[str] = []
        current = node
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        if isinstance(current, ast.Name):
            parts.append(current.id)
        parts.reverse()
        return parts


class InlineConstructor(LintRule):
    """Detect inline constructor calls on AWS service modules.

    In wetwire-aws, all property types and nested structures should be defined
    as wrapper classes with `resource:` annotations, not as inline constructor
    calls on service modules.

    Detects:
    - s3.ServerSideEncryptionConfiguration(...)
    - ec2.SecurityGroupIngress(...)
    - s3.Transition(days=30, ...)
    - Any call where the function is service.ClassName(...)

    Suggests:
    - Define a wrapper class instead:
      class MyClassName:
          resource: service.Resource.PropertyType
          # properties here

    This is a common mistake when users try to use constructor syntax instead
    of the declarative wrapper pattern.
    """

    rule_id = "WAW013"
    description = "Use wrapper classes instead of inline constructors"

    # Known AWS service modules from wetwire_aws
    AWS_SERVICE_MODULES = {
        "s3",
        "ec2",
        "lambda_",
        "iam",
        "rds",
        "dynamodb",
        "sqs",
        "sns",
        "cloudwatch",
        "logs",
        "events",
        "apigateway",
        "route53",
        "cloudfront",
        "ecs",
        "eks",
        "elasticache",
        "elasticloadbalancing",
        "elasticloadbalancingv2",
        "kms",
        "secretsmanager",
        "ssm",
        "stepfunctions",
        "cognito",
        "kinesis",
        "firehose",
        "glue",
        "athena",
        "redshift",
        "emr",
        "batch",
        "codebuild",
        "codepipeline",
        "codecommit",
        "codedeploy",
        "waf",
        "wafv2",
        "acm",
        "amplify",
        "appconfig",
        "appsync",
        "backup",
        "budgets",
        "chatbot",
        "cloudformation",
        "cloudtrail",
        "config",
        "connect",
        "datapipeline",
        "directoryservice",
        "dms",
        "docdb",
        "elasticsearch",
        "elasticmapreduce",
        "fsx",
        "gamelift",
        "greengrass",
        "guardduty",
        "inspector",
        "iot",
        "kafka",
        "lakeformation",
        "lex",
        "licensemanager",
        "lightsail",
        "macie",
        "mediaconvert",
        "medialive",
        "mediapackage",
        "mediastore",
        "msk",
        "neptune",
        "networkfirewall",
        "opsworks",
        "organizations",
        "personalize",
        "pinpoint",
        "polly",
        "qldb",
        "quicksight",
        "ram",
        "rekognition",
        "resourcegroups",
        "robomaker",
        "sagemaker",
        "servicecatalog",
        "servicediscovery",
        "ses",
        "shield",
        "signer",
        "simspaceweaver",
        "timestream",
        "transfer",
        "wafregional",
        "workspaces",
        "xray",
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for Call nodes where func is an Attribute
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    # Get the parts: for s3.Something, we get ['s3', 'Something']
                    parts = self._get_attribute_parts(node.func)

                    # Check if it's a service module call with arguments
                    if len(parts) >= 2 and parts[0] in self.AWS_SERVICE_MODULES:
                        # It's something like s3.Something(...) or s3.Bucket.Something(...)
                        # Only flag if there are arguments (empty () is handled by WAW011)
                        if node.args or node.keywords:
                            original = ast.get_source_segment(context.source, node)
                            if original:
                                service = parts[0]
                                class_name = parts[-1]

                                # Build the suggested wrapper pattern
                                if len(parts) == 2:
                                    # s3.Something -> might need s3.Bucket.Something
                                    resource_type = f"{service}.{class_name}"
                                else:
                                    # s3.Bucket.Something -> correct nesting
                                    resource_type = ".".join(parts)

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=(
                                            f"Use a wrapper class instead of inline constructor "
                                            f"{service}.{class_name}(...)"
                                        ),
                                        line=node.lineno,
                                        column=node.col_offset,
                                        original=original,
                                        suggestion=(
                                            f"# Define a wrapper class:\n"
                                            f"# class My{class_name}:\n"
                                            f"#     resource: {resource_type}\n"
                                            f"#     # ... properties ..."
                                        ),
                                        fix_imports=[],
                                    )
                                )

        return issues

    def _get_attribute_parts(self, node: ast.expr) -> list[str]:
        """Extract parts from a nested Attribute node."""
        parts: list[str] = []
        current = node
        while isinstance(current, ast.Attribute):
            parts.append(current.attr)
            current = current.value
        if isinstance(current, ast.Name):
            parts.append(current.id)
        parts.reverse()
        return parts


class InlinePolicyDocument(LintRule):
    """Detect inline IAM policy documents that should use wrapper classes.

    IAM policy documents should be expressed as wrapper classes with
    `resource: iam.PolicyDocument` or similar, not as inline dict literals.

    Detects:
    - assume_role_policy_document = {"Version": "2012-10-17", "Statement": [...]}
    - policy_document = {"Version": ..., "Statement": [...]}
    - Any dict assigned to a field ending in _policy, _policy_document, or _document
      that has "Version" and "Statement" keys

    Suggests:
    - Define wrapper classes for PolicyDocument and PolicyStatement
    """

    rule_id = "WAW014"
    description = "Use wrapper classes instead of inline policy documents"

    # Field names that typically hold policy documents
    POLICY_FIELD_PATTERNS = [
        "policy_document",
        "assume_role_policy_document",
        "key_policy",
        "bucket_policy",
        "queue_policy",
        "topic_policy",
    ]

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Check assignments
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        # Check if this looks like a policy field
                        is_policy_field = (
                            field_name in self.POLICY_FIELD_PATTERNS
                            or field_name.endswith("_policy")
                            or field_name.endswith("_policy_document")
                        )

                        if is_policy_field and isinstance(node.value, ast.Dict):
                            if self._is_policy_document(node.value):
                                original = ast.get_source_segment(
                                    context.source, node.value
                                )
                                if original:
                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=(
                                                "Use wrapper classes for policy documents. "
                                                "Define a class with 'resource: iam.PolicyDocument'"
                                            ),
                                            line=node.lineno,
                                            column=node.col_offset,
                                            original=original[:50] + "..."
                                            if len(original) > 50
                                            else original,
                                            suggestion=(
                                                "# Define wrapper classes:\n"
                                                "# class MyPolicyStatement:\n"
                                                "#     resource: iam.PolicyStatement\n"
                                                '#     effect = "Allow"\n'
                                                "#     action = [...]\n"
                                                "#     resource = [...]\n"
                                                "#\n"
                                                "# class MyPolicy:\n"
                                                "#     resource: iam.PolicyDocument\n"
                                                "#     statement = [MyPolicyStatement]"
                                            ),
                                            fix_imports=[],
                                        )
                                    )

        return issues

    def _is_policy_document(self, node: ast.Dict) -> bool:
        """Check if a dict looks like an IAM policy document.

        Policy documents have "Version" and "Statement" keys.
        """
        keys = set()
        for key in node.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                keys.add(key.value)

        return "Version" in keys and "Statement" in keys


class InlineSecurityGroupRules(LintRule):
    """Detect inline security group ingress/egress dicts that should use wrapper classes.

    Security group rules should be expressed as wrapper classes with
    `resource: ec2.SecurityGroup.Ingress` or `ec2.SecurityGroup.Egress`,
    not as inline dict literals.

    Detects:
    - security_group_ingress = [{"IpProtocol": "tcp", ...}]
    - security_group_egress = [{"IpProtocol": "-1", ...}]

    Suggests:
    - Define wrapper classes for each rule
    """

    rule_id = "WAW015"
    description = "Use wrapper classes instead of inline security group rules"

    # Field names for security group rules
    SG_RULE_FIELDS = [
        "security_group_ingress",
        "security_group_egress",
        "ingress",
        "egress",
    ]

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if field_name in self.SG_RULE_FIELDS:
                            # Check if it's a list of dicts
                            if isinstance(node.value, ast.List):
                                for elt in node.value.elts:
                                    if isinstance(elt, ast.Dict):
                                        if self._is_sg_rule(elt):
                                            original = ast.get_source_segment(
                                                context.source, elt
                                            )
                                            if original:
                                                rule_type = (
                                                    "Ingress"
                                                    if "ingress" in field_name
                                                    else "Egress"
                                                )
                                                issues.append(
                                                    LintIssue(
                                                        rule_id=self.rule_id,
                                                        message=(
                                                            f"Use wrapper class for security group {rule_type.lower()} rule"
                                                        ),
                                                        line=elt.lineno,
                                                        column=elt.col_offset,
                                                        original=original[:50] + "..."
                                                        if len(original) > 50
                                                        else original,
                                                        suggestion=(
                                                            f"# Define a wrapper class:\n"
                                                            f"# class My{rule_type}Rule:\n"
                                                            f"#     resource: ec2.SecurityGroup.{rule_type}\n"
                                                            f"#     ip_protocol = ...\n"
                                                            f"#     from_port = ...\n"
                                                            f"#     to_port = ..."
                                                        ),
                                                        fix_imports=[],
                                                    )
                                                )

        return issues

    def _is_sg_rule(self, node: ast.Dict) -> bool:
        """Check if a dict looks like a security group rule."""
        keys = set()
        for key in node.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                keys.add(key.value.lower().replace("_", ""))

        # SG rules typically have ip_protocol/IpProtocol and from_port/to_port or cidr
        has_protocol = "ipprotocol" in keys
        has_port = "fromport" in keys or "toport" in keys
        has_cidr = "cidrip" in keys or "cidr" in keys or "sourcesecuritygroupid" in keys

        return has_protocol and (has_port or has_cidr)


class InlinePolicyStatement(LintRule):
    """Detect inline IAM policy statements that should use wrapper classes.

    Policy statements inside `statement = [...]` should be wrapper classes
    with `resource: iam.PolicyStatement`, not inline dicts.

    Detects:
    - statement = [{"Effect": "Allow", "Action": [...], ...}]

    Suggests:
    - Define wrapper classes for each statement
    """

    rule_id = "WAW016"
    description = "Use wrapper classes instead of inline policy statements"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "statement":
                        # Check if it's a list of dicts
                        if isinstance(node.value, ast.List):
                            for elt in node.value.elts:
                                if isinstance(elt, ast.Dict):
                                    if self._is_policy_statement(elt):
                                        original = ast.get_source_segment(
                                            context.source, elt
                                        )
                                        if original:
                                            issues.append(
                                                LintIssue(
                                                    rule_id=self.rule_id,
                                                    message="Use wrapper class for policy statement",
                                                    line=elt.lineno,
                                                    column=elt.col_offset,
                                                    original=original[:50] + "..."
                                                    if len(original) > 50
                                                    else original,
                                                    suggestion=(
                                                        "# Define a wrapper class:\n"
                                                        "# class MyStatement:\n"
                                                        "#     resource: iam.PolicyStatement\n"
                                                        '#     effect = "Allow"\n'
                                                        "#     action = [...]\n"
                                                        "#     resource_ = [...]  # note: resource_"
                                                    ),
                                                    fix_imports=[],
                                                )
                                            )

        return issues

    def _is_policy_statement(self, node: ast.Dict) -> bool:
        """Check if a dict looks like an IAM policy statement."""
        keys = set()
        for key in node.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                keys.add(key.value.lower())

        # Statements typically have Effect and Action
        return "effect" in keys and ("action" in keys or "principal" in keys)


class InlinePropertyType(LintRule):
    """Detect inline dicts for property types that should use wrapper classes.

    Complex property types should be expressed as wrapper classes, not inline dicts.
    Uses suffix matching to detect property type fields.
    """

    rule_id = "WAW017"
    description = "Use wrapper class instead of inline property type dict"

    # Suffixes that indicate a property type field
    PROPERTY_TYPE_SUFFIXES = (
        "_configuration",
        "_configurations",
        "_config",
        "_settings",
        "_options",
        "_specification",
        "_specifications",
        "_data",
        "_profile",
        "_mappings",
        "_interfaces",
        "_parameters",
        "_properties",
        "_attributes",
        "_metadata",
        "_definition",
        "_template",
        "_encryption",
        "_rules",
        "_rule",
        "_filter",
        "_filters",
        "_expiration",
        "_transition",
        "_transitions",
        "_time",
        "_modifications",
        "_analysis",
        "_criteria",
        "_condition",
        "_export",
        "_format",
        "_types",
        "_retention",
        "_replication",
        "_translation",
        "_destination",
        "_threshold",
        "_prefix",
        "_objects",
        "_tierings",
    )

    # Fields to always flag regardless of suffix
    ALWAYS_FLAG = {
        "placement",
        "monitoring",
        "tags",
        "filter",
        "destination",
        "rule",
        "rules",
        "transition",
        "transitions",
        "tierings",
    }

    # Fields to never flag (simple dicts that are fine inline)
    NEVER_FLAG = {
        "properties",  # CloudFormation Properties block
        "parameters",  # Top-level parameters
        "outputs",  # Top-level outputs
        "conditions",  # Top-level conditions
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if self._should_flag(field_name):
                            if isinstance(node.value, ast.Dict):
                                # Skip simple dicts (1 key with simple value)
                                if len(node.value.keys) <= 1 and not self._has_complex_value(node.value):
                                    continue
                                original = ast.get_source_segment(
                                    context.source, node.value
                                )
                                if original:
                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use wrapper class for {field_name}",
                                            line=node.lineno,
                                            column=node.col_offset,
                                            original=original[:50] + "..."
                                            if len(original) > 50
                                            else original,
                                            suggestion="# Define a wrapper class with resource: <service>.<PropertyType>",
                                            fix_imports=[],
                                        )
                                    )
                            elif isinstance(node.value, ast.List):
                                # Check for list of dicts
                                for elt in node.value.elts:
                                    if isinstance(elt, ast.Dict) and len(elt.keys) > 1:
                                        original = ast.get_source_segment(
                                            context.source, elt
                                        )
                                        if original:
                                            issues.append(
                                                LintIssue(
                                                    rule_id=self.rule_id,
                                                    message=f"Use wrapper class for {field_name} item",
                                                    line=elt.lineno,
                                                    column=elt.col_offset,
                                                    original=original[:50] + "..."
                                                    if len(original) > 50
                                                    else original,
                                                    suggestion="# Define a wrapper class with resource: <service>.<PropertyType>",
                                                    fix_imports=[],
                                                )
                                            )

        return issues

    def _should_flag(self, field_name: str) -> bool:
        """Check if a field should be flagged for inline dict usage."""
        if field_name in self.NEVER_FLAG:
            return False
        if field_name in self.ALWAYS_FLAG:
            return True
        return field_name.endswith(self.PROPERTY_TYPE_SUFFIXES)

    def _has_complex_value(self, dict_node: ast.Dict) -> bool:
        """Check if a dict contains complex nested values (non-empty dicts or lists)."""
        for value in dict_node.values:
            if isinstance(value, ast.Dict) and len(value.keys) > 0:
                return True
            if isinstance(value, ast.List) and len(value.elts) > 0:
                return True
        return False
