import glob
import os
import shutil
import sys
from typing import TextIO


class Application:
    """Deletes files in a directory tree matching a glob pattern, with a
    dry-run mode that prints what would be removed without touching the
    filesystem."""

    class InvalidModeError(Exception):
        pass

    class RootDirnameError(Exception):
        pass

    @classmethod
    def run(cls, dirname: str = '.', pattern: str = '*', mode: str = 'd',
            io: TextIO | None = None) -> None:
        instance = cls(dirname=dirname, pattern=pattern, mode=mode, io=io)
        instance.validate_mode()
        instance.validate_dirname()
        instance._run()

    def __init__(self, dirname: str = '.', pattern: str = '*',
                 mode: str = 'd', io: TextIO | None = None) -> None:
        self._dirname = dirname
        self._pattern = pattern
        self._mode = mode
        self._io = io
        self._files: list[str] | None = None

    @property
    def files(self) -> list[str]:
        """Matched lazily so validation can refuse a dirname before any
        globbing happens."""
        if self._files is None:
            self._files = glob.glob(
                os.path.join(self._dirname, '**', self._pattern),
                recursive=True)
        return self._files

    def validate_mode(self) -> None:
        match self._mode:
            case 'd' | 'e':
                return
            case _:
                raise self.InvalidModeError(
                    f'{self._mode} is invalid mode. '
                    'Provide either `d`(default) or `e`.'
                )

    def validate_dirname(self) -> None:
        """Refuses filesystem roots (`/`, `C:\\`, ...) so a stray
        `file-clean` can never sweep an entire drive."""
        absolute = self._absolute_dirname()
        if os.path.dirname(absolute) == absolute:
            raise self.RootDirnameError(
                f'{absolute} is a filesystem root. '
                'Provide a narrower dirname.'
            )

    # private

    def _absolute_dirname(self) -> str:
        return os.path.abspath(self._dirname)

    def _run(self) -> None:
        self._output(
            f'Target dirname is {self._absolute_dirname()}')
        if not self.files:
            self._announce_empty()
            return
        self._announce_start()
        self._clean_files()
        self._announce_finish()

    def _announce_empty(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'No {self._pattern} Remains ==========')

    def _announce_start(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total File Count to Clean: {len(self.files)} ==========')
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Start Cleaning {self._pattern} ==========')

    def _clean_files(self) -> None:
        for file in self.files:
            self._output(
                f'========== [{self._exec_mode()}] '
                f'Cleaning {file} ==========')
        if self._mode == 'e':
            for file in self.files:
                if os.path.isdir(file):
                    shutil.rmtree(file, ignore_errors=True)
                else:
                    os.remove(file)

    def _announce_finish(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Cleaned {self._pattern} ==========')
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total Cleaned File Count: {len(self.files)} ==========')

    def _exec_mode(self) -> str:
        return 'EXECUTION' if self._mode == 'e' else 'DRY RUN'

    def _output(self, message: str) -> None:
        print(message, file=self._io if self._io is not None else sys.stdout)
