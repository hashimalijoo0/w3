
import os
import re

files = [
    "kashmir-great-lakes-trek.html",
    "tarsar-marsar-trek.html",
    "tulian-lake-trek.html",
    "gangbal-nandkol-trek.html",
    "kousarnag-trek.html",
    "sheshnag-lake-trek.html",
    "bandipora-gangbal-trek.html",
    "kolahoi-glacier-trek.html"
]

base_dir = "c:\\Users\\hashi\\w3"

def fix_buttons(filepath):
    print(f"Fixing buttons in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the Book button link.
    # It looks like:
    # <a href="..."
    #    style="...">Book</a>
    # We want to remove perfectly.
    
    # Pattern: <a [anything] >Book</a>
    # We use DOTALL to match newlines.
    # We should be careful not to match too much.
    # The button ends with </a>.
    
    pattern = r'<a\s+href="https://wa\.me/[^"]+"\s+style="[^"]+">Book</a>'
    
    # We only want to remove it inside the Booking tab.
    # Extract Booking tab content
    booking_match = re.search(r'(<div id="booking" class="detail-tab-content">)(.+?)(</div>\s*<!-- Right Column)', content, re.DOTALL)
    
    if booking_match:
        booking_content = booking_match.group(2)
        # Remove buttons from this content
        new_booking_content = re.sub(pattern, '', booking_content, flags=re.DOTALL)
        
        if new_booking_content != booking_content:
            # Replace in original content
            content = content.replace(booking_content, new_booking_content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("  - Buttons removed.")
        else:
            # Maybe the pattern didn't match due to whitespace differences?
            # Try a looser pattern.
            print("  - Pattern match failed, trying looser pattern...")
            looser_pattern = r'<a[^>]*?>Book</a>'
            new_booking_content = re.sub(looser_pattern, '', booking_content, flags=re.DOTALL)
            if new_booking_content != booking_content:
                 content = content.replace(booking_content, new_booking_content)
                 with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                 print("  - Buttons removed with looser pattern.")
            else:
                 print("  - No buttons found to remove.")
    else:
        print("  - Booking tab not found (regex issue?)")

for filename in files:
    full_path = os.path.join(base_dir, filename)
    if os.path.exists(full_path):
        fix_buttons(full_path)
    else:
        print(f"File not found: {full_path}")

print("All files fixed.")
