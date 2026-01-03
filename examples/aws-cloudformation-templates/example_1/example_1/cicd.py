"""Cicd resources: Repo."""

from . import *  # noqa: F403


class Repo:
    resource: codecommit.Repository
    repository_name = 'my-repo'
