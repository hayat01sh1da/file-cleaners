# Security Policy

## Supported Versions

- Only the latest scripts on `master` are supported.
- Historical tags or forks that diverge from the documented environment may not receive fixes.

## Ecosystem & Compatibility

| Component            | Version(s) / Tooling            | Notes |
| -------------------- | -------------------------------- | ----- |
| OS baseline          | WSL (Ubuntu 24.4.3 LTS)         | Matches the environment described in the README. |
| Ruby CLI utilities   | Ruby 4.0.1 (`.ruby-version`)    | Depend solely on the Ruby standard library; any extra gems must be declared per script. |
| Python CLI utilities | CPython 3.14.2 (`.python-version`) | Standard-library only. Add new packages via a requirements file if needed. |

## Backward Compatibility

- Command-line flags and configuration prompts remain stable across Ruby 4.0.x and Python 3.14.x releases. If a migration is required, the README will include step-by-step guidance.
- Scripts are not tested on older interpreter majors, and we do not backport security fixes to them.

## Reporting a Vulnerability

If you discover a vulnerability, please contact us privately:

1. Open a GitHub Security Advisory using **Security → Report a vulnerability** (preferred).
2. Or email `security@project.org` with a description, repro steps, and affected  script(s).

We acknowledge within **3 business days** and update you at least every **7 business days** while we investigate.  
Fixes are shipped on `master` along with mitigation guidance. Reports deemed out of scope will receive justification.
