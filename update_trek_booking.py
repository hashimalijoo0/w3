
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

packages_html = """
            <!-- Tab: Packages -->
            <div id="packages" class="detail-tab-content">
                <h2>Select Your Package</h2>
                <div class="pricing-grid" style="margin-top: 20px; gap: 20px; justify-content: center;">
                    
                    <!-- Basic Package -->
                    <div class="pricing-card" style="padding: 25px; min-width: 250px;">
                        <h3 style="color: #ccc; margin-bottom: 10px;">Basic</h3>
                        <div class="price-tag" style="font-size: 1.8rem; margin-bottom: 20px;">₹18,500</div>
                        <ul class="features-list" style="text-align: left; margin-bottom: 25px; font-size: 0.9rem;">
                            <li>Standard Dome Tents</li>
                            <li>Veg Meals (Breakfast/Dinner)</li>
                            <li>Certified Trek Leader</li>
                            <li>Basic First Aid</li>
                            <li>Sleeping Bags & Mats</li>
                        </ul>
                        <a href="https://wa.me/919622494350?text=I'm interested in the Basic Package for this trek" class="btn" style="width: 100%; padding: 12px; font-size: 1rem;">Book Basic</a>
                    </div>

                    <!-- Premium Package -->
                    <div class="pricing-card featured" style="padding: 25px; min-width: 250px; border-color: var(--accent-color);">
                        <div style="position: absolute; top: 0; right: 0; background: var(--accent-color); color: white; padding: 5px 10px; font-size: 0.8rem; font-weight: bold; border-radius: 0 10px 0 10px;">POPULAR</div>
                        <h3 style="color: white; margin-bottom: 10px;">Premium</h3>
                        <div class="price-tag" style="font-size: 1.8rem; margin-bottom: 20px;">₹24,500</div>
                        <ul class="features-list" style="text-align: left; margin-bottom: 25px; font-size: 0.9rem;">
                            <li>Premium Walk-in Tents</li>
                            <li>All Meals (Non-Veg options)</li>
                            <li>Expert Guide & Support Staff</li>
                            <li>Oxygen Cylinders</li>
                            <li>Offloading (1 Bag)</li>
                        </ul>
                        <a href="https://wa.me/919622494350?text=I'm interested in the Premium Package for this trek" class="btn" style="width: 100%; padding: 12px; font-size: 1rem;">Book Premium</a>
                    </div>

                    <!-- Luxury Package -->
                    <div class="pricing-card" style="padding: 25px; min-width: 250px;">
                        <h3 style="color: #f1c40f; margin-bottom: 10px;">Luxury</h3>
                        <div class="price-tag" style="font-size: 1.8rem; margin-bottom: 20px;">₹32,500</div>
                        <ul class="features-list" style="text-align: left; margin-bottom: 25px; font-size: 0.9rem;">
                            <li>Hotel Stay (Before/After)</li>
                            <li>Glamping Tents</li>
                            <li>Gourmet Meals</li>
                            <li>Personal Porter</li>
                            <li>Airport Transfers</li>
                        </ul>
                        <a href="https://wa.me/919622494350?text=I'm interested in the Luxury Package for this trek" class="btn" style="width: 100%; padding: 12px; font-size: 1rem;">Book Luxury</a>
                    </div>

                </div>
            </div>
"""

def update_file(filepath):
    print(f"Updates {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Tab Buttons
    # Add Packages button and Rename Booking -> Dates
    if "openDetailTab(event, 'packages')" not in content:
        # Find the line with Booking & Dates
        tabs_pattern = r'(<button class="detail-tab-btn" onclick="openDetailTab\(event, \'booking\'\)">)(Booking & Dates)(</button>)'
        
        def replace_tabs(match):
            # Insert Packages button before
            packages_btn = '\n                <button class="detail-tab-btn" onclick="openDetailTab(event, \'packages\')">Packages</button>'
            # Rename Booking button
            dates_btn = match.group(1) + "Dates & Availability" + match.group(3)
            return packages_btn + "\n                " + dates_btn

        content = re.sub(tabs_pattern, replace_tabs, content)
    
    # 2. Insert Packages Content
    # Insert before <!-- Tab: Booking -->
    if 'id="packages"' not in content:
        booking_tab_start = '<!-- Tab: Booking -->'
        if booking_tab_start in content:
            content = content.replace(booking_tab_start, packages_html + "\n\n            " + booking_tab_start)
        else:
            print(f"Warning: Could not find Booking tab start in {filepath}")

    # 3. Modify Booking Tab (Remove Book Buttons)
    # Find the booking tab content block
    # Simple approach: Replace the Book button <a> tags inside the 'booking' section?
    # Or just replace the specific button pattern globally? 
    # The 'Book' button is: <a href="https://wa.me/..." ...>Book</a>
    # We want to remove it.
    
    # Let's target the lines containing "Book</a>" inside the file
    # But ONLY inside the list of dates.
    # The list items look like:
    # <div ...>
    #    <span>Date</span>
    #    <span>Status</span>
    #    <a ...>Book</a>
    # </div>
    
    lines = content.split('\n')
    new_lines = []
    in_booking_tab = False
    
    for line in lines:
        if 'id="booking"' in line:
            in_booking_tab = True
        
        if in_booking_tab and 'id="lightbox-modal"' in line: # End of content area roughly
            in_booking_tab = False

        if in_booking_tab:
            # Check for the Book button line
            if '>Book</a>' in line and 'href="https://wa.me' in line:
                # Remove the link or comment it out?
                # User said "keep the dates section without book button"
                # If we remove the <a>, the flex layout (justify-content: space-between) implies 3 items?
                # The div has: Date, Status, Button.
                # If we remove Button, we have Date, Status.
                # space-between will push Date to left, Status to right. That looks good!
                continue # Skip this line (remove the button)
        
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # Also Check if "Booking & Dates" text inside the Tab content (Wait, the user didn't ask to rename the ID, just the button text)
    # The ID remains 'booking' for the Dates tab, which is fine, but semantically 'dates' would be better.
    # But renaming ID breaks JS 'openDetailTab'.
    # So we keep ID='booking' but button text='Dates & Availability'. 
    # And we added ID='packages'.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in files:
    full_path = os.path.join(base_dir, filename)
    if os.path.exists(full_path):
        update_file(full_path)
    else:
        print(f"File not found: {full_path}")

print("All files updated.")
