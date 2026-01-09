"""Messaging resources: CustomBus."""

from . import *  # noqa: F403


class CustomBus(events.EventBus):
    name = 'SuperBus2'
