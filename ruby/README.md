## 1. Environment

- Ruby 4.0.6
- Gemfile 4.0.16
- Bundler 4.0.16

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ rake run_file_cleaner
Provide the directory which contains files you would like to delete
.
Provide the dirname or filename pattern you would like to delete
*.rb
Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!
e
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/ruby
========== [EXECUTION] Total File Count to Clean: 2 ==========
========== [EXECUTION] Start Cleaning *.rb ==========
========== [EXECUTION] Cleaning ./src/application.rb ==========
========== [EXECUTION] Cleaning ./test/application_test.rb ==========
========== [EXECUTION] Cleaned *.rb ==========
========== [EXECUTION] Total Cleaned File Count: 2 ==========
```

## 4. Unit Test

```command
$ rake
Run options: --seed 945

# Running:

....

Finished in 5.683493s, 0.7038 runs/s, 0.8797 assertions/s.

4 runs, 5 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 2 RBS files under sig/generated
$ steep check
# Type checking files:

....

No type error detected. 🫖
```
