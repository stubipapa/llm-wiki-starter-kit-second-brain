import os
import re

wiki_dir = 'wiki'
index_file = os.path.join(wiki_dir, 'index.md')
log_file = os.path.join(wiki_dir, 'log.md')

# 1. Get all markdown files
all_md_files = []
for root, _, files in os.walk(wiki_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            if filepath not in [index_file, log_file]:
                all_md_files.append(filepath)

# 2. Extract links from index.md
index_links = []
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()
    index_links = re.findall(r'\[\[(.*?)\]\]', index_content)
    # Also extract backticks format in index.md like `- `name` — desc`
    backtick_links = re.findall(r'- `(.*?)` —', index_content)

registered_names = set(index_links + backtick_links)

# Get basenames of all files (without .md)
file_basenames = {os.path.basename(f)[:-3]: f for f in all_md_files}

# Check Index Consistency
black_household = [] # File exists but not in index
unregistered_index = [] # In index but file doesn't exist

for basename in file_basenames:
    if basename not in registered_names:
        black_household.append(basename)

for name in registered_names:
    if name not in file_basenames:
        unregistered_index.append(name)

# 3. Link Check & Conflict Check
dead_links = []
reference_count = {name: 0 for name in file_basenames}
conflicts = []

link_pattern = re.compile(r'\[\[(.*?)\]\]')

for filepath in all_md_files:
    basename = os.path.basename(filepath)[:-3]
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Conflict check
        if '## 知識衝突' in content:
            conflicts.append(basename)
            
        links = link_pattern.findall(content)
        for link in links:
            # Handle aliases [[link|alias]]
            target = link.split('|')[0]
            if target in file_basenames:
                reference_count[target] += 1
            else:
                dead_links.append((basename, target))

orphans = [name for name, count in reference_count.items() if count == 0 and name not in ['index', 'log']]

print("=== LINT RESULTS ===")
print("Black Household (Files not in index):", black_household)
print("Unregistered Index (In index, file missing):", unregistered_index)
print("Dead Links (source -> target):", dead_links)
print("Orphans (0 refs):", orphans)
print("Conflicts:", conflicts)
