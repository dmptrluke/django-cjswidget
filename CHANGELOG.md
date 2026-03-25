# Changelog

## 0.7.0 (2026-03-26)

### Changed

- **Breaking:** Upgraded vendored Choices.js from v9.0.1 to v11.2.1. No changes to the widget Python API or JavaScript initialization.
- **Breaking:** HTML in choice labels is now escaped by default (Choices.js `allowHTML` changed from `true` to `false`). Pass `allowHTML: True` in the widget options dict to restore the old behavior.
- **Breaking:** Choices.js v11 uses CSS custom properties (`--choices-*`) for theming instead of hardcoded values. If you override Choices.js styles, you may need to update your CSS.

## 0.6.0 (2026-03-25)

### Changed

- Migrated build to hatchling, linting to ruff, dependency management to uv.
- Added CI and release workflows, updated Django classifiers.
