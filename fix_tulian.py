import re

filename = "tulian-lake-trek.html"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the bad block pattern
# We look for the detail-layout div followed by the map placeholder and mobile content
# and replace it with detail-layout followed by detail-content and tabs

bad_block_pattern = r'(<div class="detail-layout">\s*<!-- Left Column: Tabs & Content -->\s*)<div[^>]*>\s*\[Map Placeholder\]\s*</div>\s*</div>\s*<!-- Altitude Profile \(Mobile Only\) -->\s*<div class="mobile-only-content">.*?</div>\s*</div>'

replacement = r'''<div class="detail-layout">
        <!-- Left Column: Tabs & Content -->
        <div class="detail-content">
            <div class="detail-tabs">
                <button class="detail-tab-btn active" onclick="openDetailTab(event, 'overview')">Overview</button>
                <button class="detail-tab-btn" onclick="openDetailTab(event, 'itinerary')">Itinerary</button>
                <button class="detail-tab-btn" onclick="openDetailTab(event, 'inclusions')">Inclusions</button>
                <button class="detail-tab-btn" onclick="openDetailTab(event, 'booking')">Booking & Dates</button>
            </div>'''

# Use regex with DOTALL to match across newlines
new_content = re.sub(bad_block_pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[SUCCESS] Fixed {filename}")
else:
    print(f"[ERROR] Could not find the bad block in {filename}")
    # Print a snippet to see what's there
    start_idx = content.find('<div class="detail-layout">')
    if start_idx != -1:
        print("Found detail-layout at index", start_idx)
        print("Next 500 chars:")
        print(content[start_idx:start_idx+500])
