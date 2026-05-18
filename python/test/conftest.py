import pytest
import glob
import os
import shutil
import sys
from collections.abc import Iterator

sys.path.append('./src')


@pytest.fixture(autouse=True)
def __cleanup_caches__() -> Iterator[None]:
    before = set(
        glob.glob(
            os.path.join(
                '.',
                '**',
                '__pycache__'),
            recursive=True))
    yield
    for pycache in before:
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


@pytest.fixture
def tmp_dir() -> Iterator[str]:
    dirname = os.path.join('.', 'test', 'tmp')
    os.makedirs(dirname, exist_ok=True)
    for i in range(1, 101):
        with open(os.path.join(dirname, f'test_file_{i:03}.txt'), 'w') as f:
            f.write('')
    yield dirname
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
