# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
