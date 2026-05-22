import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from application import Application  # noqa: E402


@task
def run_file_cleaner(c: Context) -> None:
    """Run File Cleaner"""
    print('Provide the directory which contains files you would like '
          'to delete')
    dirname = input().strip()

    print('Provide the dirname or filename pattern you would like to '
          'delete')
    pattern = input().strip()

    print('Provide d(dry_run: default) to make sure what directories '
          'and files are to be delete first. Then, provide e(execution) '
          'if you would truly like to delete the files. This operation '
          'is cannot be undone, so be alert to your operation!')
    mode = input().strip()

    params: dict[str, str] = {}
    for key, value in {
        'dirname': dirname, 'pattern': pattern, 'mode': mode,
    }.items():
        if value:
            params[key] = value

    Application(**params).run()


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
