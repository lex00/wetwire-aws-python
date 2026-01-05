"""Cicd resources: Repo."""

from . import *  # noqa: F403


class Repo(codecommit.Repository):
    repository_name = 'my-repo'
