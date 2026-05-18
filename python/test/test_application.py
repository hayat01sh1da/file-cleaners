import glob
import os

import pytest

from application import Application, InvalidModeError


PATTERN = '*.txt'


def test_invalid_mode(tmp_dir: str) -> None:
    with pytest.raises(InvalidModeError) as excinfo:
        Application(dirname=tmp_dir, pattern=PATTERN, mode='a').run()
    assert str(
        excinfo.value) == 'a is invalid mode. Provide either `d`(default) or `e`.'


@pytest.mark.parametrize('mode', [None, 'd'])
def test_run_in_dry_run_mode(tmp_dir: str, mode: str | None) -> None:
    kwargs = {'dirname': tmp_dir, 'pattern': PATTERN}
    if mode is not None:
        kwargs['mode'] = mode
    Application(**kwargs).run()
    assert len(
        glob.glob(
            os.path.join(
                tmp_dir,
                '**',
                PATTERN),
            recursive=True)) == 100


def test_run_in_exec_mode(tmp_dir: str) -> None:
    Application(dirname=tmp_dir, pattern=PATTERN, mode='e').run()
    assert len(
        glob.glob(
            os.path.join(
                tmp_dir,
                '**',
                PATTERN),
            recursive=True)) == 0
