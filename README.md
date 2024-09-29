## 1. Common Environment

- WSL(Ubuntu 20.04.6 LTS)

## 2. READMEs

- [Ruby](./ruby/README.md)
- [Python](./python/README.md)

## 3. How to Use

In you terminal, provide the following 3 parameters via interactive user inputs.

- `dirname`: The directory which contains files you would like to delete
- `pattern`: The dirname or filename pattern you would like to delete
- `mode`: The operation is done as the execution mode with `-e` and the dry_run mode without any option

### 3-1. For Ruby Lovers

```command
$ cd ./ruby/
$ ruby main.rb 
Provide the directory which contains files you would like to delete
.   
Provide the dirname or filename pattern you would like to delete
*.rb
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended

Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/ruby
========== [DRY RUN] Total File Count to Clean: 3 ==========
========== [DRY RUN] Start Cleaning *.rb ==========
========== [DRY RUN] Cleaning ./main.rb ==========
========== [DRY RUN] Cleaning ./src/application.rb ==========
========== [DRY RUN] Cleaning ./test/application_test.rb ==========
========== [DRY RUN] Cleaned *.rb ==========
========== [DRY RUN] Total Cleaned File Count: 3 ==========
```

### 3-2. For Python Lovers

```command
$ cd ./python/
$ python main.py 
Provide the directory which contains files you would like to delete: .
Provide the dirname or filename pattern you would like to delete: *.py
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended:
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/python
========== [DRY_RUN] Total File Count to Clean: 3 ==========
========== [DRY_RUN] Start Cleaning *.py ==========
========== [DRY_RUN] Cleaning ./main.py ==========
========== [DRY_RUN] Cleaning ./src/application.py ==========
========== [DRY_RUN] Cleaning ./test/test_application.py ==========
========== [DRY_RUN] Cleaned *.py ==========
========== [DRY_RUN] Total Cleaned File Count: 3 ==========
```
