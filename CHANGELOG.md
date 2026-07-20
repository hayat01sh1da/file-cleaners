# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).  
One repository hosts two packages, so releases are tagged per ecosystem (`ruby-vX.Y.Z` for the RubyGems gem, `python-vX.Y.Z` for the PyPI library).

## [0.1.1] - 2026-07-20

### 1. Fixed

- `RubyGem - Release` workflow: `ruby/setup-ruby` now resolves the Ruby version from `RubyGem/.ruby-version` instead of erroring (`input ruby-version needs to be specified…`) when `.ruby-version` existed only at the repository root, so a `ruby-v*` tag push builds and publishes the gem to completion.

### 2. Changed

- Both packages now publish automatically via Trusted Publishing (OIDC) on their release tags (`ruby-vX.Y.Z` / `python-vX.Y.Z`); `PyPI/.python-version` mirrors the RubyGem toolchain scoping for symmetry across the ecosystem directories. The packaged `file-clean` CLI and library behaviour are unchanged from 0.1.0 — this is a release-automation maintenance release.

## [0.1.0] - 2026-07-20

### 1. Added

- `file-clean` CLI with an optional `PATTERN` argument defaulting to `*`, a `--dirname` option picking the directory tree to clean (default: `.`), a `--mode d|e` flag keeping the dry run as the default and requiring an explicit `e` to delete, plus `--version` and `--help`, replacing the interactive `rake run_file_cleaner` / `invoke run_file_cleaner` prompts as the packaged entry point (Ruby and Python).
- Injectable output stream: `Application` writes its progress log to an `io` argument (default: stdout) instead of sniffing the caller stack to detect a test environment.
- Ruby gem packaging: `SpreenClean` module under `RubyGem/lib/`, `require 'spreen-clean'` shim, `spreen-clean.gemspec`, `exe/file-clean`, and RBS signatures shipped in the gem.
- Python packaging: `spreen_clean` package under `PyPI/src/`, full PyPI metadata in `pyproject.toml`, `file-clean` console script, and the `py.typed` marker.
- The spreen-clean brand icon (`assets/spreen-clean-icon.svg`): the origami falcon sweeping scattered files off a malachite stone.
- Filesystem-root refusal: a dirname resolving to `/` (or a drive root like `C:\`) raises `RootDirnameError` before anything is scanned, so a stray `file-clean` can never sweep an entire drive (Ruby and Python).
- Bulk-delete confirmation: the execution mode asks for an explicit `y` when more than 100 files match, with a `--yes` flag to skip the prompt for scripted use (CLI, Ruby and Python).

### 2. Changed

- Named the packages **`spreen-clean`** per the `spreen-<function>` family naming, following the repository rename from `file-cleaners` (2026-07-17): RubyGem `spreen-clean` (`SpreenClean`), PyPI `spreen-clean` (`spreen_clean`), CLI `file-clean`.
- Renamed the ecosystem directories and workflow prefixes — `ruby/` → `RubyGem/` (`Ruby - *` → `RubyGem - *` workflows) and `python/` → `PyPI/` (`Python - *` → `PyPI - *`) — aligning the CI and daily-update workflows with the `rubygem--release.yml` / `pypi--release.yml` release-workflow convention.
- READMEs document the safety model (dry run by default, explicit `--mode e` to execute, root refusal, bulk-delete confirmation) and the packaged installation (`gem install spreen-clean` / `pipx install spreen-clean`) in-repo, and the Actions Status badges point at the renamed repository.
- The matched file list is computed lazily and exposed as a public `files` reader, so dirname validation runs before any globbing and the CLI can inspect the match count for the bulk-delete confirmation.

### 3. Removed

- Flat `RubyGem/src/` and `PyPI/src/application.py` script layouts and the interactive Rake/Invoke tasks (superseded by the packages and the CLI above); the `invoke` dependency is gone.
