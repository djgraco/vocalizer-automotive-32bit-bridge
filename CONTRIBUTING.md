# Contributing

Choose the branch matching the intended variant: `main` for the classic bridge,
`brokered-audio` for experimental audio routing, or `legacy-2.1.6-2025` for the
native NVDA 2025 compatibility version. Keep variant-specific runtime behavior
separate. This maintenance change standardizes build infrastructure, not synthesis.

Follow [building instructions](docs/building.md). Run source/package checks and
the existing tests where present. Record actual Windows/NVDA tests separately
from automated checks; do not change compatibility claims without testing.

Preserve original author notices and the distinction between GPL driver code
and engine components. Do not commit personal license files or voice packages.
For translations, see [the translation workflow](addon/locale/README.md).
