"""Command line interface behind the `file-clean` executable:
`file-clean [PATTERN] [--dirname DIR] [--mode d|e] [--yes]`."""

import argparse
import sys

from . import __version__
from .application import Application

# The execution mode asks for confirmation above this many matches.
BULK_DELETE_THRESHOLD = 100


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='file-clean',
        description='Delete files in a directory tree matching a glob '
                    'pattern, dry run first.')
    parser.add_argument(
        'pattern', nargs='?', default='*', metavar='PATTERN',
        help='Dirname or filename glob pattern to clean (default: *)')
    parser.add_argument(
        '--dirname', default='.',
        help='Directory tree to clean (default: .)')
    parser.add_argument(
        '--mode', choices=('d', 'e'), default='d',
        help='Operation mode (d = dry run, e = execute, default: d)')
    parser.add_argument(
        '--yes', action='store_true',
        help='Skip the bulk-delete confirmation in the execution mode')
    parser.add_argument('--version', action='version', version=__version__)
    return parser


def _confirmed(application: Application, mode: str, skip: bool) -> bool:
    """Guards the execution mode against oversized sweeps: above
    BULK_DELETE_THRESHOLD matches it asks for an explicit `y`, unless
    `--yes` was given for scripted use."""
    if mode != 'e' or skip:
        return True
    count = len(application.files)
    if count <= BULK_DELETE_THRESHOLD:
        return True
    try:
        answer = input(
            f'About to delete {count} files '
            f'(more than {BULK_DELETE_THRESHOLD}). Type `y` to proceed: ')
    except EOFError:
        return False
    return answer.strip().lower() in ('y', 'yes')


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    application = Application(
        dirname=args.dirname, pattern=args.pattern, mode=args.mode)
    try:
        application.validate_mode()
        application.validate_dirname()
    except (Application.InvalidModeError,
            Application.RootDirnameError) as error:
        print(error, file=sys.stderr)
        return 1
    if not _confirmed(application, args.mode, args.yes):
        print('Aborted the execution mode without deleting anything.',
              file=sys.stderr)
        return 1
    application._run()
    return 0


if __name__ == '__main__':
    sys.exit(main())
