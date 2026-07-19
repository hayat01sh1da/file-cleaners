import glob
import io
import os

import pytest

from spreen_clean import Application


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


def test_run_announces_the_dry_run_progress(tmp_dir: str) -> None:
    stream = io.StringIO()
    Application.run(dirname=tmp_dir, pattern=PATTERN, io=stream)
    output = stream.getvalue()
    assert f'Target dirname is {os.path.abspath(tmp_dir)}' in output
    assert ('========== [DRY RUN] '
            'Total File Count to Clean: 100 ==========') in output
    cleaning = os.path.join(tmp_dir, 'test_file_001.txt')
    assert f'========== [DRY RUN] Cleaning {cleaning} ==========' in output


def test_run_announces_the_execution_progress(tmp_dir: str) -> None:
    stream = io.StringIO()
    Application.run(dirname=tmp_dir, pattern=PATTERN, mode='e', io=stream)
    output = stream.getvalue()
    assert '========== [EXECUTION] Start Cleaning *.txt ==========' in output
    assert '========== [EXECUTION] Cleaned *.txt ==========' in output
    assert ('========== [EXECUTION] '
            'Total Cleaned File Count: 100 ==========') in output


def test_run_announces_empty_when_nothing_matches(tmp_dir: str) -> None:
    stream = io.StringIO()
    Application.run(dirname=tmp_dir, pattern='*.log', io=stream)
    assert ('========== [DRY RUN] '
            'No *.log Remains ==========') in stream.getvalue()


def test_run_refuses_a_filesystem_root() -> None:
    stream = io.StringIO()
    with pytest.raises(Application.RootDirnameError) as excinfo:
        Application.run(dirname='/', pattern=PATTERN, io=stream)
    assert str(excinfo.value) == (
        '/ is a filesystem root. Provide a narrower dirname.'
    )
    assert stream.getvalue() == ''
