## 1. Environment

- Python 3.14.4

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ python main.py
Provide the directory which contains files you would like to delete: .
Provide the dirname or filename pattern you would like to delete: *.py
Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!: e
Target dirname is /mnt/c/Users/binlh/Documents/web/file-extensions-converter/python
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/python
========== [EXECUTION] Total File Count to Clean: 3 ==========
========== [EXECUTION] Start Cleaning *.py ==========
========== [EXECUTION] Cleaning ./main.py ==========
========== [EXECUTION] Cleaning ./src/application.py ==========
========== [EXECUTION] Cleaning ./test/test_application.py ==========
========== [EXECUTION] Cleaned *.py ==========
========== [EXECUTION] Total Cleaned File Count: 3 ==========
```

## 4. Unit Test

```command
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/file-cleaners/python
configfile: pyproject.toml
collected 4 items

test/test_application.py ....                                            [100%]

============================== 4 passed in 2.18s ===============================
