"""Merge Agenta's bundled template catalog with the OpenEXA agent-team catalog.

Agenta's own templates stay exactly as they are; the OpenEXA templates are appended after them. In the API
container the OpenEXA packages are mounted at <catalog dir>/openexa/packages, so their catalog paths are
rewritten to point there. Standard library only (runs on the VM with plain python3).

Usage: python3 merge_templates.py <agenta catalog.json> <openexa catalog.json> <merged catalog.json out>
"""
import json
import sys
from pathlib import Path

agenta_path, openexa_path, out_path = map(Path, sys.argv[1:4])
agenta = json.loads(agenta_path.read_text(encoding="utf-8"))
openexa = json.loads(openexa_path.read_text(encoding="utf-8"))

merged = {"schema_version": agenta["schema_version"], "templates": dict(agenta["templates"])}
for key, record in openexa["templates"].items():
    if key in merged["templates"]:
        sys.exit(f"template key {key!r} exists in both catalogs; OpenEXA keys must stay unique (prefix openexa-)")
    record = dict(record)
    record["versions"] = {version: f"openexa/{path}" for version, path in record["versions"].items()}
    merged["templates"][key] = record

# Written in place (same file), so a running container's bind mount sees the new content.
with open(out_path, "w", encoding="utf-8") as handle:
    handle.write(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
print(f"merged catalog: {len(agenta['templates'])} Agenta + {len(openexa['templates'])} OpenEXA = {len(merged['templates'])} templates")
