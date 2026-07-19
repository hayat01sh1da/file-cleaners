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


def test_root_dirname_refused(capsys: pytest.CaptureFixture[str]) -> None:
    status = main([PATTERN, '--dirname', '/', '--mode', 'e'])

    assert status == 1
    assert 'is a filesystem root' in capsys.readouterr().err


def test_bulk_execution_aborts_when_declined(
        tmp_dir: str, capsys: pytest.CaptureFixture[str],
        monkeypatch: pytest.MonkeyPatch) -> None:
    _make_bulk_files(tmp_dir)
    prompts: list[str] = []

    def decline(prompt: str) -> str:
        prompts.append(prompt)
        return 'n'

    monkeypatch.setattr('builtins.input', decline)
    status = main([PATTERN, '--dirname', tmp_dir, '--mode', 'e'])

    assert status == 1
    assert prompts == [
        'About to delete 101 files (more than 100). Type `y` to proceed: ']
    assert 'Aborted the execution mode' in capsys.readouterr().err
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 101


def test_bulk_execution_proceeds_when_confirmed(
        tmp_dir: str, monkeypatch: pytest.MonkeyPatch) -> None:
    _make_bulk_files(tmp_dir)
    monkeypatch.setattr('builtins.input', lambda prompt: 'y')
    status = main([PATTERN, '--dirname', tmp_dir, '--mode', 'e'])

    assert status == 0
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 0


def test_bulk_execution_skips_confirmation_with_yes_flag(
        tmp_dir: str, capsys: pytest.CaptureFixture[str]) -> None:
    _make_bulk_files(tmp_dir)
    status = main([PATTERN, '--dirname', tmp_dir, '--mode', 'e', '--yes'])

    assert status == 0
    assert 'About to delete' not in capsys.readouterr().out
    assert len(glob.glob(
        os.path.join(tmp_dir, '**', PATTERN), recursive=True)) == 0


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as excinfo:
        main(['--version'])

    assert excinfo.value.code == 0
    assert capsys.readouterr().out == f'{__version__}\n'


def _make_bulk_files(tmp_dir: str) -> None:
    """Tops the fixture up beyond BULK_DELETE_THRESHOLD (101 in total)."""
    for i in range(101, 102):
        with open(os.path.join(tmp_dir, f'test_file_{i:03}.txt'), 'w') as f:
            f.write('')
