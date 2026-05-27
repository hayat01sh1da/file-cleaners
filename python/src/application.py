import glob
import inspect
import os
import shutil


class Application:
    """Deletes files in a directory tree matching a glob pattern, with a
    dry-run mode that prints what would be removed without touching the
    filesystem."""

    class InvalidModeError(Exception):
        pass

    @classmethod
    def run(cls, dirname: str = '.', pattern: str = '*',
            mode: str = 'd') -> None:
        instance = cls(dirname=dirname, pattern=pattern, mode=mode)
        instance.validate_mode()
        instance._run()

    def __init__(self, dirname: str = '.', pattern: str = '*',
                 mode: str = 'd') -> None:
        self._dirname = dirname
        self._pattern = pattern
        self._mode = mode
        self._files = glob.glob(
            os.path.join(dirname, '**', pattern), recursive=True)

    def validate_mode(self) -> None:
        match self._mode:
            case 'd' | 'e':
                return
            case _:
                raise self.InvalidModeError(
                    f'{self._mode} is invalid mode. '
                    'Provide either `d`(default) or `e`.'
                )

    # private

    def _run(self) -> None:
        self._output(
            f'Target dirname is {os.path.abspath(self._dirname)}')
        if not self._files:
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
            f'Total File Count to Clean: {len(self._files)} ==========')
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Start Cleaning {self._pattern} ==========')

    def _clean_files(self) -> None:
        for file in self._files:
            self._output(
                f'========== [{self._exec_mode()}] '
                f'Cleaning {file} ==========')
        if self._mode == 'e':
            for file in self._files:
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
            f'Total Cleaned File Count: {len(self._files)} ==========')

    def _exec_mode(self) -> str:
        return 'EXECUTION' if self._mode == 'e' else 'DRY RUN'

    def _test_env(self) -> bool:
        stack = inspect.stack()
        if not stack:
            return False
        return 'pytest' in os.path.basename(stack[-1].filename)

    def _output(self, message: str) -> None:
        if not self._test_env():
            print(message)
