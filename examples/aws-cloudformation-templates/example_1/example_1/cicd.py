"""Cicd resources: Repo."""

from . import *  # noqa: F403


class Repo(codecommit.Repository):
    resource: codecommit.Repository
    repository_name = 'my-repo'
