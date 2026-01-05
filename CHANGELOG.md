# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
