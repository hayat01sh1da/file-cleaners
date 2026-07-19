import glob
import os

import pytest

from spreen_clean import __version__
from spreen_clean.cli import main


PATTERN = '*.txt'


def test_dry_run_by_default(
        tmp_dir: str, capsys: pytest.CaptureFixture[str]) -> None:
    status = main([PATTERN, '--dirname', tmp_dir])

    assert status == 0
    assert ('========== [DRY RUN] '
            'Total File Count to Clean: 100 =========='
            ) in capsys.readouterr().out
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 100


def test_execution_mode(
        tmp_dir: str, capsys: pytest.CaptureFixture[str]) -> None:
    status = main([PATTERN, '--dirname', tmp_dir, '--mode', 'e'])

    assert status == 0
    assert ('========== [EXECUTION] '
            'Total Cleaned File Count: 100 =========='
            ) in capsys.readouterr().out
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 0


def test_default_pattern_matches_everything(
        tmp_dir: str, capsys: pytest.CaptureFixture[str]) -> None:
    status = main(['--dirname', tmp_dir])

    assert status == 0
    assert ('========== [DRY RUN] '
            'Total File Count to Clean: 100 =========='
            ) in capsys.readouterr().out
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 100


def test_invalid_mode(tmp_dir: str) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main([PATTERN, '--dirname', tmp_dir, '--mode', 'a'])

    assert excinfo.value.code == 2
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 100


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(['--version'])

    assert excinfo.value.code == 0
    assert capsys.readouterr().out == f'{__version__}\n'
