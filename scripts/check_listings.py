"""Check every product folder has the files directories need and a valid server.json.

Run: python3 scripts/check_listings.py
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["README.md", "TOOLS.md", "server.json", "glama.json", "llms-install.md", "examples"]
problems = []

for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and (p / "server.json").exists()):
    if folder.name == "_template":
        continue
    for name in REQUIRED:
        if not (folder / name).exists():
            problems.append(f"{folder.name}: missing {name}")
    if not (folder / "icon.png").exists():
        print(f"warning: {folder.name}: no icon.png (Cline and Claude need one)")
    server = json.loads((folder / "server.json").read_text())
    for key in ["name", "title", "description", "version", "websiteUrl"]:
        if not server.get(key):
            problems.append(f"{folder.name}: server.json has no {key}")
    if len(server.get("description", "")) > 100:
        problems.append(f"{folder.name}: description is over 100 characters")
    if server.get("repository", {}).get("subfolder") != folder.name:
        problems.append(f"{folder.name}: repository.subfolder should be {folder.name}")
    if not server.get("remotes") and not server.get("packages"):
        problems.append(f"{folder.name}: server.json needs remotes or packages")
    if "PRODUCT_" in (folder / "server.json").read_text():
        problems.append(f"{folder.name}: template placeholders left in server.json")

try:
    import jsonschema
    import urllib.request

    schema_url = "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"
    schema = json.load(urllib.request.urlopen(schema_url, timeout=20))
    for path in sorted(ROOT.glob("*/server.json")):
        if path.parent.name == "_template":
            continue
        try:
            jsonschema.validate(json.loads(path.read_text()), schema)
        except jsonschema.ValidationError as err:
            problems.append(f"{path.parent.name}: {err.message}")
except ImportError:
    print("warning: jsonschema not installed; skipped schema validation")

for p in problems:
    print("error:", p)
sys.exit(1 if problems else 0)
