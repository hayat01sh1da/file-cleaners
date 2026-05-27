import glob
import os

import pytest

from application import Application


PATTERN = '*.txt'


def test_invalid_mode(tmp_dir: str) -> None:
    with pytest.raises(Application.InvalidModeError) as excinfo:
        Application.run(dirname=tmp_dir, pattern=PATTERN, mode='a')
    assert str(excinfo.value) == (
        'a is invalid mode. Provide either `d`(default) or `e`.'
    )


def test_run_in_dry_run_mode_with_default_mode(tmp_dir: str) -> None:
    Application.run(dirname=tmp_dir, pattern=PATTERN)
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 100


def test_run_in_dry_run_mode_with_explicit_d_mode(tmp_dir: str) -> None:
    Application.run(dirname=tmp_dir, pattern=PATTERN, mode='d')
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 100


def test_run_in_exec_mode(tmp_dir: str) -> None:
    Application.run(dirname=tmp_dir, pattern=PATTERN, mode='e')
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 0
