## 1. Environment

- Ruby 4.0.2

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ ruby main.rb
Provide the directory which contains files you would like to delete
.
Provide the dirname or filename pattern you would like to delete
*.rb
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended
e
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/ruby
========== [EXECUTION] Total File Count to Clean: 3 ==========
========== [EXECUTION] Start Cleaning *.rb ==========
========== [EXECUTION] Cleaning ./main.rb ==========
========== [EXECUTION] Cleaning ./src/application.rb ==========
========== [EXECUTION] Cleaning ./test/application_test.rb ==========
========== [EXECUTION] Cleaned *.rb ==========
========== [EXECUTION] Total Cleaned File Count: 3 ==========
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
Inspecting 5 files.....


5 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 3 RBS files under sig/generated
$ steep check
# Type checking files:

......

No type error detected. 🫖
```
