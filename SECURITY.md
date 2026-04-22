## Supported Versions

- Only the latest scripts on `master` are supported.
- Historical tags or forks that diverge from the documented environment may not receive fixes.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling               | Notes                                                                                   |
| -------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- |
| OS baseline          | WSL (Ubuntu 25.10)                 | Shared environment across tracks.                                                       |
| Ruby CLI utilities   | Ruby 4.0.3 (`.ruby-version`)       | Depend solely on the Ruby standard library; any extra gems must be declared per script. |
| Python CLI utilities | CPython 3.14.4 (`.python-version`) | Standard-library only. Add new packages via a requirements file if needed.              |

## Backward Compatibility

- Command-line flags and configuration prompts remain stable across Ruby 4.0.x and Python 3.14.x releases. If a migration is required, the README will include step-by-step guidance.
- Scripts are not tested on older interpreter majors, and we do not backport security fixes to them.

## Reporting a Vulnerability

Please report issues privately via **GitHub Security Advisory** (preferred) — open through the repository’s **Security → Report a vulnerability** workflow.

Acknowledgement occurs and status updates follow as soon as possible.  
After remediation we publish guidance alongside required dependency updates.
