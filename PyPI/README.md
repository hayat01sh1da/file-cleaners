## 1. Environment

- Python 3.14.6
- pip 26.1.2

## 2. Installation

```command
$ pipx install spreen-clean
```

(`pip install spreen-clean` works too if you prefer managing the environment yourself.)

For development, install the dependencies via requirements.txt:

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ file-clean '*.log' --dirname ./tmp
Target dirname is /home/hayat01sh1da/workspace/tmp
========== [DRY RUN] Total File Count to Clean: 2 ==========
========== [DRY RUN] Start Cleaning *.log ==========
========== [DRY RUN] Cleaning ./tmp/app.log ==========
========== [DRY RUN] Cleaning ./tmp/jobs/worker.log ==========
========== [DRY RUN] Cleaned *.log ==========
========== [DRY RUN] Total Cleaned File Count: 2 ==========
```

The dry run above is the default. Once the list looks right, execute the deletion with `--mode e` (this cannot be undone):

```command
$ file-clean '*.log' --dirname ./tmp --mode e
Target dirname is /home/hayat01sh1da/workspace/tmp
========== [EXECUTION] Total File Count to Clean: 2 ==========
========== [EXECUTION] Start Cleaning *.log ==========
========== [EXECUTION] Cleaning ./tmp/app.log ==========
========== [EXECUTION] Cleaning ./tmp/jobs/worker.log ==========
========== [EXECUTION] Cleaned *.log ==========
========== [EXECUTION] Total Cleaned File Count: 2 ==========
```

With no arguments, `file-clean` dry-runs every file under the current directory (`PATTERN` defaults to `*`, `--dirname` to `.`).

Two guardrails back the dry-run default: a dirname resolving to a filesystem root (`/`, `C:\`, ...) is refused before anything is scanned, and when the execution mode matches more than 100 files the CLI asks for an explicit `y` first — pass `--yes` to skip the prompt in scripts:

```command
$ file-clean '*.log' --dirname ./tmp --mode e
About to delete 101 files (more than 100). Type `y` to proceed: n
Aborted the execution mode without deleting anything.
```

As a library:

```python
from spreen_clean import Application

Application.run(dirname='./tmp', pattern='*.log')            # dry run
Application.run(dirname='./tmp', pattern='*.log', mode='e')  # execute

# The progress log goes to stdout by default; pass any text stream to capture it.
import io
stream = io.StringIO()
Application.run(dirname='./tmp', pattern='*.log', io=stream)
stream.getvalue()  # => 'Target dirname is ...\n========== [DRY RUN] ...'
```

## 4. Unit Test

```command
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: spreen-clean/PyPI
configfile: pyproject.toml
collected 17 items

test/test_application.py ........                                        [ 47%]
test/test_cli.py .........                                               [100%]

============================== 17 passed in 0.42s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
Success: no issues found in 6 source files
```

## 7. Build

```command
$ python -m build
$ pipx install ./dist/spreen_clean-0.1.0-py3-none-any.whl
```
