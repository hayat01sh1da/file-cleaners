"""Command line interface behind the `file-clean` executable:
`file-clean [PATTERN] [--dirname DIR] [--mode d|e]`."""

import argparse
import sys

from . import __version__
from .application import Application


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
    parser.add_argument('--version', action='version', version=__version__)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        Application.run(
            dirname=args.dirname, pattern=args.pattern, mode=args.mode)
    except Application.InvalidModeError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
