import glob
import os

trek_files = glob.glob("*-trek.html")
broken_files = []

print("Checking trek files for structure...")
for filename in trek_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    missing = []
    if 'class="detail-tabs"' not in content:
        missing.append("detail-tabs")
    if 'class="detail-content"' not in content:
        missing.append("detail-content")
        
    if missing:
        print(f"[ERROR] {filename} is missing: {', '.join(missing)}")
        broken_files.append(filename)
    else:
        print(f"[OK] {filename} is OK")

if not broken_files:
    print("\nAll trek files have correct structure!")
else:
    print(f"\nFound {len(broken_files)} broken files.")
