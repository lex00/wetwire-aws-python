# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- WAW022: Circular dependency detection lint rule (#100)
  - Detects cycles in resource dependency graphs
  - Reports all resources involved in the cycle
  - Uses DFS for efficient cycle detection
- WAW021: Secret pattern detection lint rule (#101)
  - Detects AWS access keys and secret keys
  - Detects private key headers
  - Detects API tokens (GitHub, Slack, OpenAI, Anthropic)
  - Detects passwords and credentials by variable name
  - Ignores placeholder values
- `testing.semantic_compare` module for round-trip testing (#104)
  - `semantic_equal()`: Check if two structures are semantically equal
  - `semantic_compare()`: Get list of differences with full paths
  - `SemanticDiff`: Dataclass describing each difference
  - Ignores key ordering in dicts, preserves order in lists
- `diff` and `watch` CLI commands per spec 4.0 (#105)
  - `diff PATH --output FILE`: Compare generated output vs existing template
  - `diff PATH --output FILE --semantic`: Ignore formatting, compare structure
  - `watch PATH`: Auto-rebuild on file changes with debouncing
  - `watch PATH --lint-only`: Only run lint, skip rebuild
- Attribution README for imported AWS example templates (#106)
  - Documents source repositories for CloudFormation and SAM templates
  - Includes license information (Apache 2.0)
  - Lists import scripts for regenerating examples
- CONTRIBUTING.md with contributor guidelines (#117)
  - Development setup instructions
  - Code style guidelines (ruff, type checking)
  - Pull request process

### Changed

- CI now explicitly reports test coverage with XML output (#107)
  - Added `--cov-report=xml` for future coverage service integration
  - Added `--cov-fail-under=70` to enforce minimum coverage threshold
  - Coverage report visible in CI output

## [1.9.1] - 2026-01-09

### Fixed

- SAM import coverage improved from 40 to 58 templates (#93)
  - Templates with cookiecutter only in Description/Metadata fields now import
  - Jinja control structures (`{%...%}`) are properly excluded
  - Matches Go implementation's coverage for non-templated SAM examples

## [1.9.0] - 2026-01-09

### Added

- New `graph` CLI command for dependency visualization (#87)
  - Generate Graphviz DOT format: `wetwire-aws graph ./infra`
  - Generate Mermaid format: `wetwire-aws graph ./infra -f mermaid`
  - Cluster by AWS service: `wetwire-aws graph ./infra -c`
  - Include parameters: `wetwire-aws graph ./infra -p`
  - Different edge styles for Ref vs GetAtt references
- Added `graphviz` package dependency for DOT generation
- Added `sam-python-crud-sample` repo to SAM import sources (#91)

### Fixed

- Importer now handles SAM implicit resources gracefully (#88)
  - Templates referencing auto-created SAM resources now import successfully
  - Generates explicit `GetAtt()` / `Ref()` for implicit resources with noqa comments
  - `depends_on` uses string literals for implicit resources
- SAM import coverage improved from 39 to 40 templates (#91)
  - Changed from directory-based to content-based cookiecutter filtering
  - Templates in cookiecutter directories without `{{cookiecutter` syntax now import
  - Added third SAM template repository

## [1.8.8] - 2026-01-08

### Fixed

- WAW017 now detects single-key dicts with complex nested values
  - Previously skipped all single-key dicts regardless of value complexity
  - Now flags `bucket_encryption = {"ServerSideEncryptionConfiguration": [...]}`

## [1.8.7] - 2026-01-08

### Fixed

- WAW017 now detects 25+ additional PropertyType field suffixes (#85)
  - New suffixes: `_configurations`, `_rules`, `_rule`, `_filter`, `_filters`, etc.
  - New ALWAYS_FLAG fields: `filter`, `destination`, `rule`, `rules`, `transition`, etc.

## [1.8.6] - 2026-01-08

### Fixed

- Kiro agent now follows explicit lint-fix-relint loop
  - Added visual flowchart showing mandatory loop
  - Clear rules: never build until lint passes with zero errors
  - Reinforced "Fix → Lint → Fix → Lint → ... → Build" pattern

## [1.8.5] - 2026-01-08

### Added

- Kiro agent prompt now includes PropertyType examples (#80)
  - Adds "6. NESTED PROPERTY TYPES" section with wrapper class examples
  - Documents `<Service>.<Resource>.<PropertyType>` pattern

### Changed

- Replaced pyright with ty in typing tests (#77)
  - Tests now use project's standard type checker
  - Simplified error checking logic

### Fixed

- Kiro agent prompt now reinforces lint-before-build workflow (#78)
  - Added "Golden Rules" section at top of prompt
  - Explicit lint-build cycle in Design Workflow
  - Lint reminder in "Continuing Work" section
- WAW017 now detects `bucket_encryption` as inline property type (#79)
  - Added `_encryption` suffix to property type detection

## [1.8.4] - 2026-01-08

### Added

- Type stub file `base.pyi` for IDE support of `.Arn` attributes (#75)
  - Declares `ResourceMeta.__getattr__` returning `AttrRef` for type checkers
  - Enables IDE resolution of patterns like `MyBucket.Arn`

## [1.7.2] - 2026-01-07

### Fixed

- PropertyType wrapper classes now serialize correctly (#68)
  - Bug: `_instantiate_property_type_wrapper()` read from instance `__dict__` (empty) instead of class `__dict__` (where user values are defined)
  - Nested PropertyTypes like `BucketEncryption`, `KeySchema`, `SecurityGroupIngress` were serializing as `{}`
  - All 12 complex imported examples now generate valid CloudFormation output

### Added

- Integration tests for CloudFormation output validation (#68)
  - `TestExamplesGenerateCF` verifies imported examples generate valid CF output
  - Checks resource count matches and no empty dicts in nested Properties

## [1.7.1] - 2026-01-07

### Added

- `wetwire-aws build` command now accepts optional positional path argument (#52)
  - Example: `wetwire-aws build ./my-stack/` instead of `wetwire-aws build --module my_stack`
  - Works with relative and absolute paths
  - Validates that path is a Python package (has `__init__.py`)

### Fixed

- SAM `serverless` module now included in `resources.__all__` (#54)
  - Fixes `NameError: name 'serverless' is not defined` when importing SAM templates
- Simplify topological sort with identity comparison (#66)
  - Update dataclass-dsl dependency to >=1.1.0
  - Use class identity instead of name-based comparison for dependency detection

## [1.7.0] - 2026-01-06

### Changed

- **Breaking:** Template elements now use inheritance pattern like Resources (#47)
  - Old: `class MyParam: resource: Parameter`
  - New: `class MyParam(Parameter):`
  - Applies to Parameter, Output, Mapping, and Condition classes
  - Enables consistent syntax across all template elements
- Auto-registration for template elements in `setup_resources()`
  - No explicit decorator needed for Parameter, Output, Mapping, Condition subclasses
- Importer codegen generates inheritance pattern for all template elements

### Fixed

- Inheritance-based resource classes now include `resource:` annotation for `auto_decorate` detection (#48)
  - Imported examples were producing empty CloudFormation templates
  - Resources now have both inheritance (for `_resource_type`) and annotation (for `auto_decorate`)
- Added build verification step to `import_aws_samples.py` to catch resource registration regressions
- Fixed `test_version` test to not check for hardcoded version number
- Fixed `test_test_invalid_persona` to accept either error message

## [1.6.0] - 2026-01-05

### Added

- AWS SAM (Serverless Application Model) resource type support (#28)
  - 9 SAM resource types: `Function`, `Api`, `HttpApi`, `SimpleTable`, `LayerVersion`, `StateMachine`, `Application`, `Connector`, `GraphQLApi`
  - SAM-specific enums: `Runtime`, `Architecture`, `PackageType`, `AuthType`, `HttpApiAuthType`
  - Full PropertyType support for nested SAM structures (events, auth configs, etc.)
  - SAM Transform header automatically included in templates
- `codegen/sam_spec.py` - Static SAM resource definitions
- `scripts/generate_serverless.py` - Script to regenerate serverless package
- `scripts/import_sam_samples.py` - Import SAM templates from official AWS repos
- 85 new tests for SAM functionality across 4 test files
- SAM documentation in Quick Start guide

### Changed

- `codegen/parse.py` - Now loads SAM resources alongside CloudFormation resources
- `codegen/generate.py` - Added "serverless" service mapping
- `codegen/extract_enums.py` - Handles missing botocore service gracefully

## [1.5.0] - 2026-01-05

### Added

- `PropertyTypeProxy` class for chained attribute access on nested GetAtt patterns (#25)
- `PropertyTypeDescriptor` to wrap PropertyTypes in resources for seamless nested access
- Nested GetAtt patterns now use dot syntax: `MyDB.Endpoint.Address` instead of `GetAtt("MyDB", "Endpoint.Address")`

### Changed

- Codegen now uses `PropertyTypeDescriptor` when attaching PropertyTypes to resource classes
- Importer generates no-parens pattern for all GetAtt references including nested attributes
- Linter rules WAW006/WAW020 now flag explicit GetAtt for nested attributes (can be auto-fixed)
- Regenerated 263 resource modules and 261 example packages with new pattern

## [1.4.0] - 2026-01-05

### Changed

- **Breaking:** Wrapper classes now use inheritance pattern instead of `resource:` annotation
  - Old: `class MyBucket: resource: s3.Bucket`
  - New: `class MyBucket(s3.Bucket):`
  - Enables full IDE field suggestions and autocomplete
- Importer codegen now generates inheritance pattern for resource wrappers
- Regenerated 261 AWS CloudFormation example packages with inheritance pattern

### Added

- `ResourceMeta` metaclass for `__getattr__` support on resource classes
- Empty resource classes now generate `pass` to avoid syntax errors

### Fixed

- Nested GetAtt patterns like `Resource.Endpoint.Address` now correctly generate explicit `GetAtt()` intrinsics (#22)
  - PropertyType class attributes (e.g., `Endpoint`) shadow metaclass `__getattr__`, preventing no-parens pattern
  - Linter rules WAW006/WAW020 now skip nested attributes to avoid incorrectly converting them

## [1.3.0] - 2026-01-05

### Changed

- Importer: removed Ref/GetAtt fallback generation (now raises `ValueError` for unknown references)
- Importer: `Sub("${Param}")` now simplifies to direct reference `Param`
- Importer: `Sub("${AWS::Region}")` now simplifies to constant `AWS_REGION`
- Regenerated 261 AWS CloudFormation example packages

## [1.2.0] - 2026-01-05

### Added

- `wetwire-aws design` command: AI-assisted interactive infrastructure design
- `wetwire-aws test` command: automated persona-based testing with AI
- CLI documentation for design and test commands
- README section on AI-assisted design

## [1.1.0] - 2026-01-05

### Added

- Integration tests for importer: validates 12 complex AWS templates compile successfully
- Enhanced name sanitization: handles hyphens and invalid Python identifiers
  - `Port-1ICMP` → `PortNeg1ICMP` (hyphen before digit becomes "Neg")
  - `my-resource` → `myResource` (hyphen between letters capitalizes next)
- WAW019 linter rule: detects explicit `Ref("...")` patterns (prefer direct variable refs)
- WAW020 linter rule: detects explicit `GetAtt("...", "...")` patterns (prefer `Resource.Attr`)

### Fixed

- Variable names with hyphens now sanitized to valid Python identifiers

## [1.0.1] - 2026-01-04

### Changed

- Replace mypy and pyright with ty (Astral's type checker)
- Update CI workflows to use uv instead of pip
- Update documentation to use uv syntax

### Dependencies

- dataclass-dsl: 1.0.0 → 1.0.1
- wetwire-core: 1.0.0 → 1.0.1
- Added: ty>=0.0.1a0
- Removed: mypy, pyright

## [1.0.0] - 2026-01-03

### Changed

- **BREAKING**: Upgraded to dataclass-dsl 1.0.0 and wetwire-core 1.0.0
- Updated Development Status to Production/Stable

### Dependencies

- dataclass-dsl: 0.1.4 → 1.0.0
- wetwire-core: 0.1.0 → 1.0.0

## [0.3.3] - 2026-01-02

### Added

- PyPI publish workflow with trusted publishing (OIDC)

### Fixed

- Synchronized `__version__` in `__init__.py` with package version

## [0.2.0] - 2026-01-01

### Changed

- **BREAKING**: PropertyType submodules now use PascalCase to match CloudFormation spec naming
  - Before: `s3.bucket.BucketEncryption`, `ec2.security_group.Ingress`
  - After: `s3.Bucket.BucketEncryption`, `ec2.SecurityGroup.Ingress`
- PropertyTypes are now attached to resource classes, so `s3.Bucket.TagFilter` works even when accessing via the class

### Removed

- Deleted obsolete `docs/research/PythonGoAlignment.md` research document

## [0.1.5] - 2024-12-15

### Added

- Initial release with AWS CloudFormation resource generation
- Support for all CloudFormation resource types
- Intrinsic functions (Ref, GetAtt, Sub, Join, etc.)
- CloudFormation template importer
- Linter with AWS-specific rules
