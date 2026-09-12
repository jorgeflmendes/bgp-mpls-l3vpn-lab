#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import re

parser = argparse.ArgumentParser()
parser.add_argument("template", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()

def replace(match: re.Match[str]) -> str:
    value = os.environ.get(match.group(1))
    if not value or "\n" in value or "\r" in value:
        raise ValueError(f"{match.group(1)} is required")
    return value

text = re.sub(r"\{\{([A-Z][A-Z0-9_]*)\}\}", replace, args.template.read_text(encoding="utf-8"))
args.output.write_text(text, encoding="utf-8")
