# Using wetwire-aws with Kiro CLI

This guide walks you through setting up wetwire-aws with Kiro CLI for AI-assisted infrastructure design in AWS corporate environments.

## Prerequisites

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/) package manager
- [Kiro CLI](https://kiro.dev/docs/cli/) installed

---

## Step 1: Install wetwire-aws with Kiro Support

Install wetwire-aws with the `[kiro]` optional dependency:

```bash
uv add "wetwire-aws[kiro]"
```

This installs:
- `wetwire-aws` - CloudFormation synthesis from Python
- `mcp` - Model Context Protocol server support

Verify the installation:

```bash
uv run wetwire-aws --version
```

---

## Step 2: Install Kiro CLI

If you haven't already installed Kiro CLI, follow the [official installation guide](https://kiro.dev/docs/cli/).

Verify Kiro is installed:

```bash
kiro-cli --version
```

---

## Step 3: Configure Kiro for wetwire-aws

The first time you run `wetwire-aws design --provider kiro`, it automatically installs the required configurations:

1. **Agent config** (`~/.kiro/agents/wetwire-runner.json`) - Defines the wetwire-runner agent with access to wetwire-aws tools
2. **MCP config** (`.kiro/mcp.json` in your project) - Configures the wetwire-aws-mcp server

You can also configure these manually:

### Manual Agent Configuration

Create `~/.kiro/agents/wetwire-runner.json`:

```json
{
  "name": "wetwire-runner",
  "description": "Infrastructure code generator using wetwire-aws",
  "allowedTools": ["fs_read", "fs_write", "bash", "mcp:wetwire-aws-mcp"],
  "context": {
    "patterns": "Resources are Python classes inheriting from generated types...",
    "workflow": "1. Explore 2. Plan 3. Implement 4. Lint 5. Build"
  }
}
```

### Manual MCP Configuration

Create `.kiro/mcp.json` in your project directory:

```json
{
  "mcpServers": {
    "wetwire-aws-mcp": {
      "command": "uv",
      "args": ["run", "wetwire-aws-mcp"]
    }
  }
}
```

> **Note**: Using `uv run` ensures the MCP server command is available in your project's virtual environment.

---

## Step 4: Run Design Mode with Kiro

Start an AI-assisted design session using Kiro:

```bash
uv run wetwire-aws design --provider kiro "Create an S3 bucket with versioning"
```

Or start an interactive session without a prompt:

```bash
uv run wetwire-aws design --provider kiro
```

### Options

| Option | Description |
|--------|-------------|
| `prompt` | Initial prompt describing what to build (optional) |
| `-p, --provider` | AI provider: `anthropic` (default) or `kiro` |
| `-o, --output` | Output directory (default: current directory) |

---

## Step 5: Verify Generated Code

After the design session creates your infrastructure code, verify it:

```bash
# Lint the generated code
uv run wetwire-aws lint ./my_package

# Build the CloudFormation template
uv run wetwire-aws build ./my_package > template.json

# Preview the template
cat template.json
```

---

## MCP Tools Available to Kiro

The wetwire-aws-mcp server exposes three tools to the Kiro agent:

| Tool | Description |
|------|-------------|
| `wetwire_init` | Initialize a new wetwire-aws package |
| `wetwire_lint` | Lint Python code for wetwire-aws issues (WAW001-WAW020) |
| `wetwire_build` | Generate CloudFormation template from a package |

These tools enable the Kiro agent to:
1. Create new infrastructure packages
2. Validate code follows wetwire-aws patterns
3. Generate CloudFormation templates

---

## Example Workflow

Here's a complete workflow for creating a Lambda function with an S3 trigger:

```bash
# 1. Create a new project directory
mkdir my-lambda-project && cd my-lambda-project

# 2. Initialize a Python project with uv
uv init

# 3. Add wetwire-aws with Kiro support
uv add "wetwire-aws[kiro]"

# 4. Run design mode with Kiro
uv run wetwire-aws design --provider kiro "Create a Lambda function that processes files uploaded to an S3 bucket"

# 5. After the session, verify the generated code
uv run wetwire-aws lint .
uv run wetwire-aws build . > template.json

# 6. Deploy to AWS
aws cloudformation deploy \
  --template-file template.json \
  --stack-name my-lambda-stack \
  --capabilities CAPABILITY_IAM
```

---

## wetwire-aws Code Patterns

The Kiro agent follows these wetwire-aws patterns when generating code:

### Resource Declaration
```python
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "my-data"
```

### Direct References
```python
class MyFunction(lambda_.Function):
    role = MyRole.Arn  # GetAtt via attribute access
```

### Type-Safe Constants
```python
class MyFunction(lambda_.Function):
    runtime = lambda_.Runtime.PYTHON3_12  # Not "python3.12"
```

### Nested Types
```python
class MyEnv(lambda_.Environment):
    variables = MyVariables

class MyVariables:
    BUCKET = MyBucket
```

---

## Troubleshooting

### Kiro CLI not found

```
Error: Kiro CLI not found. Install from https://kiro.dev/docs/cli/
```

Ensure Kiro CLI is installed and in your PATH.

### MCP package not installed

```
Error: Kiro integration requires mcp package. Install with: pip install wetwire-aws[kiro]
```

Reinstall with the kiro extras:

```bash
uv add "wetwire-aws[kiro]"
```

### wetwire-aws-mcp command not found or MCP server not loading

If Kiro reports "One or more mcp server did not load correctly", the issue is usually that the `wetwire-aws-mcp` command isn't found in PATH. The auto-generated MCP config uses `uv run` to solve this:

```json
{
  "mcpServers": {
    "wetwire-aws-mcp": {
      "command": "uv",
      "args": ["run", "wetwire-aws-mcp"]
    }
  }
}
```

Verify the MCP server works:

```bash
uv run wetwire-aws-mcp --help
```

If you have an older config using just `"command": "wetwire-aws-mcp"`, update it to use `uv run` as shown above.

---

## Comparison: Kiro vs Anthropic Provider

| Feature | `--provider kiro` | `--provider anthropic` |
|---------|-------------------|------------------------|
| API | AWS Kiro CLI | Anthropic API |
| Authentication | AWS credentials | `ANTHROPIC_API_KEY` |
| Dependency | Kiro CLI + mcp | wetwire-core |
| Best for | Corporate AWS environments | Direct Anthropic access |

## Known Limitations

### Automated Testing

The Kiro provider's automated tests (`wetwire-aws test --provider kiro`) run scenarios in single-shot mode rather than simulating full multi-turn conversations. This is due to kiro-cli's architecture which requires a TTY for interactive mode.

**What this means:**
- Interactive usage (`wetwire-aws design --provider kiro`) works fully with back-and-forth conversation
- Automated persona tests send an enhanced prompt with persona characteristics and let kiro complete the task autonomously
- The Anthropic provider can simulate full conversations in tests; the Kiro provider cannot

This limitation only affects automated testing. Developers using the interactive design mode get the full conversational experience.

---

## See Also

- [Quick Start](QUICK_START.md) - Basic wetwire-aws usage
- [CLI Reference](CLI.md) - Full CLI documentation
- [Kiro CLI Docs](https://kiro.dev/docs/cli/) - Official Kiro documentation
