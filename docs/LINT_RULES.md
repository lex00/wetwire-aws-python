# Lint Rules Reference

wetwire-aws includes a linter with 19 rules (WAW001-WAW020, excluding WAW009) that enforce declarative patterns and catch common mistakes.

## Quick Reference

| Rule | Description | Auto-Fix |
|------|-------------|:--------:|
| [WAW001](#waw001-stringshouldbeparametertype) | Use parameter type constants | Yes |
| [WAW002](#waw002-refshouldBepseudoparameter) | Use pseudo-parameter constants | Yes |
| [WAW003](#waw003-stringshouldbeenum) | Use enum constants | Yes |
| [WAW004](#waw004-dictshouldbeintrinsic) | Use intrinsic function classes | Yes |
| [WAW005](#waw005-unnecessarytodict) | Remove `.to_dict()` calls | Yes |
| [WAW006](#waw006-refshouldbenoparens) | Use no-parens references | Yes |
| [WAW007](#waw007-explicitresourceimport) | Use flat imports | Yes |
| [WAW008](#waw008-verboseinitimports) | Remove verbose imports | Yes |
| [WAW010](#waw010-filetoolarge) | Split large files | No |
| [WAW011](#waw011-propertytypeasref) | No-parens for PropertyTypes | Yes |
| [WAW012](#waw012-duplicateresource) | Detect duplicate resources | No |
| [WAW013](#waw013-inlineconstructor) | Use wrapper classes | No |
| [WAW014](#waw014-inlinepolicydocument) | Use wrapper for policies | No |
| [WAW015](#waw015-inlinesecuritygrouprules) | Use wrapper for SG rules | No |
| [WAW016](#waw016-inlinepolicystatement) | Use wrapper for statements | No |
| [WAW017](#waw017-inlinepropertytype) | Use wrapper for property types | No |
| [WAW018](#waw018-redundantrelativeimport) | Remove redundant imports | No |
| [WAW019](#waw019-explicitrefintrinsic) | Avoid explicit `Ref()` | Yes |
| [WAW020](#waw020-explicitgetattintrinsic) | Avoid explicit `GetAtt()` | Yes |

---

## Type Safety Rules (WAW001-003)

### WAW001: StringShouldBeParameterType

Use parameter type constants instead of string literals.

```python
# Bad
class BucketName(Parameter):
    type = "String"

# Good
class BucketName(Parameter):
    type = STRING
```

**Why:** Type constants are validated at import time and provide IDE autocomplete.

**Available constants:** `STRING`, `NUMBER`, `LIST_NUMBER`, `COMMA_DELIMITED_LIST`, `SSM_PARAMETER_STRING`, `SSM_PARAMETER_STRING_LIST`, `AVAILABILITY_ZONE`, `LIST_AVAILABILITY_ZONE`, `AMI_ID`, `INSTANCE_ID`, `KEY_PAIR`, `SECURITY_GROUP_ID`, `LIST_SECURITY_GROUP_ID`, `SUBNET_ID`, `LIST_SUBNET_ID`, `VPC_ID`, `VOLUME_ID`, `HOSTED_ZONE_ID`

---

### WAW002: RefShouldBePseudoParameter

Use pseudo-parameter constants instead of `Ref("AWS::...")`.

```python
# Bad
region = Ref("AWS::Region")

# Good
region = AWS_REGION
```

**Why:** Constants are shorter, typo-proof, and semantically clear.

**Available constants:** `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_STACK_NAME`, `AWS_STACK_ID`, `AWS_PARTITION`, `AWS_URL_SUFFIX`, `AWS_NO_VALUE`, `AWS_NOTIFICATION_ARNS`

---

### WAW003: StringShouldBeEnum

Use enum constants instead of string literals for known CloudFormation values.

```python
# Bad
class MyFunction(lambda_.Function):
    runtime = "python3.12"

# Good
class MyFunction(lambda_.Function):
    runtime = lambda_.Runtime.PYTHON3_12
```

**Why:** Enums catch typos at import time and provide IDE autocomplete for valid values.

**Common enums:**
- `lambda_.Runtime.*` - Lambda runtimes
- `lambda_.Architecture.*` - CPU architectures
- `s3.ServerSideEncryption.*` - Encryption algorithms
- `dynamodb.KeyType.*` - DynamoDB key types
- `dynamodb.ScalarAttributeType.*` - Attribute types

---

## Intrinsic Function Rules (WAW004-005, WAW019-020)

### WAW004: DictShouldBeIntrinsic

Use intrinsic function classes instead of raw dictionaries.

```python
# Bad
bucket_name = {"Ref": "MyBucket"}
role_arn = {"Fn::GetAtt": ["MyRole", "Arn"]}

# Good
bucket_name = Ref("MyBucket")
role_arn = GetAtt("MyRole", "Arn")

# Best (see WAW019/WAW020)
bucket_name = MyBucket
role_arn = MyRole.Arn
```

**Why:** Intrinsic classes validate arguments and provide better IDE support.

---

### WAW005: UnnecessaryToDict

Remove unnecessary `.to_dict()` calls on intrinsic functions.

```python
# Bad
bucket_name = Ref("MyBucket").to_dict()

# Good
bucket_name = Ref("MyBucket")
```

**Why:** Serialization happens automatically during template generation.

---

### WAW019: ExplicitRefIntrinsic

Avoid explicit `Ref()` - use direct variable references.

```python
# Bad
vpc_id = Ref(MyVPC)

# Good
vpc_id = MyVPC
```

**Why:** Direct references are cleaner and enable static dependency analysis.

---

### WAW020: ExplicitGetAttIntrinsic

Avoid explicit `GetAtt()` - use attribute access.

```python
# Bad
role_arn = GetAtt(MyRole, "Arn")

# Good
role_arn = MyRole.Arn
```

**Why:** Attribute access is cleaner and validates the attribute exists.

---

## Reference Style Rules (WAW006, WAW011)

### WAW006: RefShouldBeNoParens

Use no-parens references instead of `ref()` helper.

```python
# Bad
vpc_id = ref(MyVPC)
role_arn = get_att(MyRole, "Arn")

# Good
vpc_id = MyVPC
role_arn = MyRole.Arn
```

**Why:** No-parens style enables static analysis and is more readable.

---

### WAW011: PropertyTypeAsRef

Use no-parens style for PropertyType wrapper references.

```python
# Bad
class MyBucket(s3.Bucket):
    bucket_encryption = MyEncryption()

# Good
class MyBucket(s3.Bucket):
    bucket_encryption = MyEncryption
```

**Why:** PropertyTypes are configuration, not instantiated objects.

---

## Import Rules (WAW007-008, WAW018)

### WAW007: ExplicitResourceImport

Use flat imports with module-qualified names instead of explicit resource imports.

```python
# Bad
from wetwire_aws.resources.s3 import Bucket

class MyBucket(Bucket):
    pass

# Good
from . import *

class MyBucket(s3.Bucket):
    pass
```

**Why:** Flat imports with `from . import *` are handled by `setup_resources()` and provide all AWS modules.

---

### WAW008: VerboseInitImports

Remove verbose imports in `__init__.py` that `setup_params()`/`setup_resources()` handle.

```python
# Bad (in __init__.py)
from wetwire_aws.template import Parameter, Output
from wetwire_aws.params import STRING, NUMBER

# Good
from wetwire_aws.loader import setup_params, setup_resources
setup_params(globals())  # Injects Parameter, Output, STRING, etc.
```

**Why:** The loader functions inject all needed symbols automatically.

---

### WAW018: RedundantRelativeImport

Remove redundant relative imports when using `from . import *`.

```python
# Bad
from . import *
from . import MyBucket  # Redundant

# Good
from . import *
```

**Why:** Star import already includes all exported symbols.

---

## File Organization Rules (WAW010, WAW012)

### WAW010: FileTooLarge

Split files with more than 15 resources into smaller, categorized files.

```
# Bad: main.py with 25 resources

# Good: Split by category
storage.py    # S3, EFS
compute.py    # Lambda, EC2
network.py    # VPC, subnets
security.py   # IAM roles
database.py   # DynamoDB, RDS
```

**Categories:**
- `storage` - S3, EFS, FSx, Backup
- `compute` - Lambda, EC2 (Instance, Volume), ECS, EKS
- `network` - VPC, EC2 (VPC, Subnet, SecurityGroup), Route53
- `security` - IAM, KMS, SecretsManager, WAF
- `database` - RDS, DynamoDB, ElastiCache, Neptune
- `messaging` - SNS, SQS, EventBridge
- `main` - Everything else

---

### WAW012: DuplicateResource

Detect duplicate resource class names within a file.

```python
# Bad
class MyBucket(s3.Bucket):
    bucket_name = "one"

class MyBucket(s3.Bucket):  # Duplicate!
    bucket_name = "two"
```

**Why:** Duplicate names cause the second definition to silently override the first.

---

## Declarative Style Rules (WAW013-017)

These rules enforce the "wrapper class" pattern central to wetwire-aws.

### WAW013: InlineConstructor

Use wrapper classes instead of inline constructors.

```python
# Bad
class MyBucket(s3.Bucket):
    bucket_encryption = s3.Bucket.BucketEncryption(
        server_side_encryption_configuration=[...]
    )

# Good
class MyBucketEncryption(s3.Bucket.BucketEncryption):
    server_side_encryption_configuration = [MyEncryptionRule]

class MyBucket(s3.Bucket):
    bucket_encryption = MyBucketEncryption
```

**Why:** Wrapper classes are declarative, reusable, and easier to read.

---

### WAW014: InlinePolicyDocument

Use wrapper classes for policy documents.

```python
# Bad
class MyRole(iam.Role):
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [...]
    }

# Good
class MyAssumeRolePolicy(PolicyDocument):
    version = "2012-10-17"
    statement = [MyAssumeRoleStatement]

class MyRole(iam.Role):
    assume_role_policy_document = MyAssumeRolePolicy
```

---

### WAW015: InlineSecurityGroupRules

Use wrapper classes for security group ingress/egress rules.

```python
# Bad
class MySG(ec2.SecurityGroup):
    security_group_ingress = [
        {"IpProtocol": "tcp", "FromPort": 443, "ToPort": 443, ...}
    ]

# Good
class HttpsIngress(ec2.SecurityGroup.Ingress):
    ip_protocol = "tcp"
    from_port = 443
    to_port = 443
    cidr_ip = "0.0.0.0/0"

class MySG(ec2.SecurityGroup):
    security_group_ingress = [HttpsIngress]
```

---

### WAW016: InlinePolicyStatement

Use wrapper classes for policy statements.

```python
# Bad
class MyPolicy(PolicyDocument):
    statement = [
        {"Effect": "Allow", "Action": "s3:*", "Resource": "*"}
    ]

# Good
class S3AllowStatement(PolicyStatement):
    effect = "Allow"
    action = "s3:*"
    resource = "*"

class MyPolicy(PolicyDocument):
    statement = [S3AllowStatement]
```

---

### WAW017: InlinePropertyType

Use wrapper classes for property type dictionaries.

```python
# Bad
class MyTable(dynamodb.Table):
    key_schema = [
        {"AttributeName": "pk", "KeyType": "HASH"}
    ]

# Good
class MyKeySchema(dynamodb.Table.KeySchema):
    attribute_name = "pk"
    key_type = dynamodb.KeyType.HASH

class MyTable(dynamodb.Table):
    key_schema = [MyKeySchema]
```

---

## Running the Linter

```bash
# Lint a file or directory
wetwire-aws lint myapp/

# Auto-fix issues
wetwire-aws lint myapp/ --fix

# Verbose output
wetwire-aws lint myapp/ -v
```

## See Also

- [CLI Reference](CLI.md) - Full CLI documentation
- [Quick Start](QUICK_START.md) - Getting started guide
