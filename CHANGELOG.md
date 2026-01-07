# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
