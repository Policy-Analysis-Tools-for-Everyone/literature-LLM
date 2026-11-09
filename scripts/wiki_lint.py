#!/usr/bin/env python3
"""Small, dependency-free check of local Markdown links in the wiki/protocol."""
from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
refs = []
for folder in ('wiki', 'protocol'):
    for file in (root / folder).rglob('*.md'):
        text = file.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
            if target.startswith(('https:', 'http:', 'mailto:', '#')):
                continue
            local = target.split('#', 1)[0].split('?', 1)[0]
            if not local:
                continue
            if not (file.parent / local).resolve().exists():
                refs.append(f'{file.relative_to(root)} -> {target}')
if refs:
    print('Broken local links:')
    print('\n'.join(refs))
    sys.exit(1)
print('OK: local Markdown links resolve.')
