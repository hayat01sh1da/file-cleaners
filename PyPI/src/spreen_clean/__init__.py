"""Spreens your workspace clean — the falcon's stoop, then the preen:
deletes files in a directory tree matching a glob pattern, defaulting to a
dry run that prints what would be removed before anything is touched."""

from .application import Application

__version__ = '0.1.0'

__all__ = [
    'Application',
    '__version__',
]
