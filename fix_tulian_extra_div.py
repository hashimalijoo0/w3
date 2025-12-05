import re

filename = "tulian-lake-trek.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: </div> followed by <!-- Tab: Overview -->
# We want to remove the </div>
pattern = r'(</div>\s*<!-- Tab: Overview -->)'
# But wait, the </div> is indented.
# Let's look for the specific sequence
#             </div>
#     </div>
#             <!-- Tab: Overview -->

# We want to keep the first </div> (closing detail-tabs) and remove the second one.

target = '            </div>\n    </div>\n            <!-- Tab: Overview -->'
replacement = '            </div>\n            <!-- Tab: Overview -->'

if target in content:
    new_content = content.replace(target, replacement)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[SUCCESS] Fixed extra div in {filename}")
else:
    # Try with regex to be more flexible with whitespace
    pattern = r'(</div>\s*)</div>(\s*<!-- Tab: Overview -->)'
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\1\2', content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[SUCCESS] Fixed extra div in {filename} using regex")
    else:
        print(f"[ERROR] Could not find the target block in {filename}")
        # Print context
        idx = content.find('<!-- Tab: Overview -->')
        if idx != -1:
            print("Context:")
            print(content[idx-50:idx+50])
