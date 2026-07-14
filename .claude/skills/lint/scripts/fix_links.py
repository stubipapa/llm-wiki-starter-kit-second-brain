import os
import re

wiki_dir = 'wiki'

replacements = {
    r'\[\[superpowers\]\]': '[[Superpowers]]',
    r'\[\[spectra\]\]': '[[Spectra]]',
    r'\[\[openspec\]\]': '[[OpenSpec]]',
    r'\[\[superpowers\|': '[[Superpowers|',
    r'\[\[spectra\|': '[[Spectra|',
    r'\[\[openspec\|': '[[OpenSpec|'
}

count = 0
for root, _, files in os.walk(wiki_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = re.sub(old, new, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed links in {filepath}")

print(f"Fixed {count} files.")
