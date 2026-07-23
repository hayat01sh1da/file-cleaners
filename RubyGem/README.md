## 1. Environment

- Ruby 4.0.6
- Gemfile 4.0.17
- Bundler 4.0.17

## 2. Installation

```command
$ gem install spreen-clean
```

For development, install the dependencies via Gemfile and Bundler:

```command
$ bundle install
$ bundle lock --add-checksums
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

```ruby
require 'spreen_clean' # or require 'spreen-clean'

SpreenClean::Application.run(dirname: './tmp', pattern: '*.log')            # dry run
SpreenClean::Application.run(dirname: './tmp', pattern: '*.log', mode: 'e') # execute

# The progress log goes to stdout by default; pass any IO to capture it.
require 'stringio'
io = StringIO.new
SpreenClean::Application.run(dirname: './tmp', pattern: '*.log', io:)
io.string # => "Target dirname is ...\n========== [DRY RUN] ..."
```

## 4. Unit Test

```command
$ rake
Run options: --seed 4809

# Running:

..................

Finished in 13.872874s, 1.2975 runs/s, 4.1088 assertions/s.

18 runs, 57 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ bundle exec rubocop
Inspecting 12 files
............

12 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ bundle exec rbs-inline --output sig/generated/ .
🎉 Generated 7 RBS files under sig/generated
$ bundle exec steep check
# Type checking files:

..............

No type error detected. 🫖
```

## 7. Build

```command
$ gem build spreen-clean.gemspec
$ gem install ./spreen-clean-0.1.0.gem
```
