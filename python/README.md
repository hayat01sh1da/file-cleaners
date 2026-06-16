## 1. Environment

- Python 3.14.6
- pip 26.1.2

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ invoke run_file_cleaner
Provide the directory which contains files you would like to delete
.
Provide the dirname or filename pattern you would like to delete
*.py
Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!
e
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/ruby
========== [EXECUTION] Total File Count to Clean: 2 ==========
========== [EXECUTION] Start Cleaning *.py ==========
========== [EXECUTION] Cleaning ./src/application.rb ==========
========== [EXECUTION] Cleaning ./test/application_test.rb ==========
========== [EXECUTION] Cleaned *.py ==========
========== [EXECUTION] Total Cleaned File Count: 2 ==========
```

## 4. Unit Test

```command
$ invoke
============================= test session starts ==============================
platform linux -- Python 3.14.6, pytest-9.0.3, pluggy-1.6.0
rootdir: file-cleaners/python
configfile: pyproject.toml
collected 4 items

test/test_application.py ....                                            [100%]

============================== 4 passed in 2.54s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
./src/application.py:39:80: E501 line too long (86 > 79 characters)
./src/application.py:65:80: E501 line too long (88 > 79 characters)
./test/test_application.py:16:80: E501 line too long (82 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ mypy .
Success: no issues found in 4 source files
```
