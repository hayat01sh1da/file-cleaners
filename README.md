[![Actions Status: PyPI - CI](https://github.com/hayat01sh1da/spreen-clean/workflows/PyPI%20-%20CI/badge.svg)](https://github.com/hayat01sh1da/spreen-clean/actions?query=workflow%3A%22PyPI%20-%20CI%22)
[![Actions Status: PyPI - Daily Dependencies Update](https://github.com/hayat01sh1da/spreen-clean/workflows/PyPI%20-%20Daily%20Dependencies%20Update/badge.svg)](https://github.com/hayat01sh1da/spreen-clean/actions?query=workflow%3A%22PyPI%20-%20Daily%20Dependencies%20Update%22)
[![Actions Status: RubyGem - CI](https://github.com/hayat01sh1da/spreen-clean/workflows/RubyGem%20-%20CI/badge.svg)](https://github.com/hayat01sh1da/spreen-clean/actions?query=workflow%3A%22RubyGem%20-%20CI%22)
[![Actions Status: RubyGem - Daily Dependencies Update](https://github.com/hayat01sh1da/spreen-clean/workflows/RubyGem%20-%20Daily%20Dependencies%20Update/badge.svg)](https://github.com/hayat01sh1da/spreen-clean/actions?query=workflow%3A%22RubyGem%20-%20Daily%20Dependencies%20Update%22)
[![Actions Status: CodeQL](https://github.com/hayat01sh1da/spreen-clean/workflows/CodeQL/badge.svg)](https://github.com/hayat01sh1da/spreen-clean/actions?query=workflow%3A%22CodeQL%22)

# spreen-clean

<img src="./assets/spreen-clean-icon.svg" align="center" width="300" alt="spreen-clean: an origami falcon sweeping scattered files off a malachite stone, leaving a polished gleam in its wake" />

## 1. Overview

**spreen-clean** — the falcon's stoop, then the preen — deletes files in a directory tree matching a glob pattern, dry run first.  
It ships as a RubyGems gem and a PyPI library, both installing the same `file-clean` CLI.

The icon tells the story: the origami falcon (隼 /hayabusa/) mid-sweep across the malachite stone, scattered files dissolving ahead of its dive and a polished gleam left in its wake — the workspace, settled.  
The full legend behind the `spreen` name is told in [spreen-wiki's README](https://github.com/hayat01sh1da/spreen-wiki#1-origin-of-the-name).

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

Part of the `spreen-*` toolchain ([spreen-wiki](https://github.com/hayat01sh1da/spreen-wiki), [spreen-pr](https://github.com/hayat01sh1da/spreen-pr), [spreen-tracks](https://github.com/hayat01sh1da/spreen-tracks), spreen-clean): tools that take something scattered and return it settled.

## 2. Safety Model

The tool is opinionated about safety: **every run is a dry run until you say otherwise.**

|Mode |Meaning |Filesystem |
|:-|:-|:-|
|`d` (default) |Dry run |Prints every file that would be removed; nothing is touched. |
|`e` |Execution |Deletes every printed file. This cannot be undone. |

Any other mode fails with a clear error instead of guessing.

## 3. Installation

Install from either ecosystem — the CLI is identical:

```command
$ gem install spreen-clean
```

```command
$ pipx install spreen-clean
```

(`pip install spreen-clean` works too if you prefer managing the environment yourself.)

## 4. Usage

```command
$ file-clean [PATTERN] [options]
```

- `PATTERN` is the dirname or filename glob to clean; with no `PATTERN`, everything under the target directory matches (`*`).
- `--dirname DIR` sets the directory tree to clean (default: the current directory); the pattern matches recursively beneath it.
- `--mode d|e` picks the operation mode — dry run by default; pass `e` to actually delete what the dry run printed:

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

- `--version` prints the version; `--help` prints the usage.

Both packages also expose the logic as a library — see the per-language READMEs below.

## 5. Development

- Common environment: WSL (Ubuntu 25.10)
- [Ruby README](./RubyGem/README.md) / [Ruby sources](./RubyGem/)
- [Python README](./PyPI/README.md) / [Python sources](./PyPI/)
