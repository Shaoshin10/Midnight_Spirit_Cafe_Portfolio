#!/usr/bin/env python3
"""Verhindert versehentliche Veröffentlichung privater Godot-Projektdateien."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_FILE_NAMES = {
    "project.godot",
    "export_presets.cfg",
    "main.gd",
}

FORBIDDEN_DIRECTORY_NAMES = {
    ".godot",
    "scenes",
    "scripts",
    "data",
    "addons",
}

FORBIDDEN_SUFFIXES = {
    ".tscn",
    ".scn",
    ".tres",
    ".res",
    ".uid",
    ".save",
    ".tmp",
}

IGNORED_DIRECTORY_NAMES = {
    ".git",
}

ALLOWED_GDSCRIPT_DIRECTORY = ROOT / "code_samples"


def is_inside(path: Path, directory: Path) -> bool:
    try:
        path.resolve().relative_to(directory.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    violations: list[str] = []

    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)

        if any(part in IGNORED_DIRECTORY_NAMES for part in relative.parts):
            continue

        if path.is_dir():
            if path.name in FORBIDDEN_DIRECTORY_NAMES:
                violations.append(f"Verbotener Projektordner: {relative}")
            continue

        if path.name in FORBIDDEN_FILE_NAMES:
            violations.append(f"Verbotene Projektdatei: {relative}")

        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            violations.append(f"Verbotener Godot-/Projektdateityp: {relative}")

        if path.suffix.lower() == ".gd" and not is_inside(
            path,
            ALLOWED_GDSCRIPT_DIRECTORY,
        ):
            violations.append(
                f"GDScript außerhalb des freigegebenen Beispielordners: {relative}"
            )

    if violations:
        print("Portfolio-Sicherheitsprüfung FEHLGESCHLAGEN:\n")
        for violation in sorted(set(violations)):
            print(f"- {violation}")
        return 1

    print("Portfolio-Sicherheitsprüfung OK.")
    print("Keine typischen privaten Godot-Projektdateien gefunden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
