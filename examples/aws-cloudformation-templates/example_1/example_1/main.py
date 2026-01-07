"""Stack resources."""

from . import *  # noqa: F403


class AddReadme(CloudFormationResource):
    # Unknown resource type: Boto3::CodeCommit.put_file
    repository_name = Repo.Name
    branch_name = 'master'
    file_content = 'Hello, world'
    file_path = 'README.md'
    commit_message = 'Add another README.md'
    name = 'CloudFormation'
