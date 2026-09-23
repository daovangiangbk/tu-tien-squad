#!/usr/bin/env bash
# Shim → geographic-builder skill scripts
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL_SCRIPTS="$(cd "$HERE/../../.cursor/skills/geographic-builder/scripts" && pwd)"
exec "$SKILL_SCRIPTS/render_stack.sh" "$@"
