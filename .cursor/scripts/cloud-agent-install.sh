#!/usr/bin/env bash
set -euo pipefail

# tu-tien-squad: markdown content repo — no package dependencies.
# Validates canonical layout so agents can read Foundation, Logic, and Interface layers.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

required=(
  foundation/core/00-glossary.md
  foundation/core/01-theme-tragedy-core.md
  projects/README.md
  projects/active-work.md
  .cursor/agents/xianxia-prose-writer.md
  .cursor/rules/three-layer-xianxia-novel.mdc
)

for path in "${required[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "Missing required path: $path" >&2
    exit 1
  fi
done

active_work="$(tr -d '[:space:]' < projects/active-work.md)"
if [[ -z "$active_work" ]]; then
  echo "projects/active-work.md is empty" >&2
  exit 1
fi

if [[ ! -d "projects/${active_work}" ]]; then
  echo "Active work slug '${active_work}' has no project directory" >&2
  exit 1
fi

echo "tu-tien-squad repository structure validated (active work: ${active_work})."
