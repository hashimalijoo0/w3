import re

# Overview content for each trek
overview_data = {
    "tulian-lake-trek.html": {
        "history": """Tulian Lake sits in a dramatic amphitheater between the Zanskar and Pir Panjal ranges. Historically,
                    it was a summer grazing region for local herders. The lake was discovered by trekkers in the early
                    20th century and later made famous for its bowl-shaped glacier setting. Despite its proximity to
                    Pahalgam, it remains relatively less crowded, offering an authentic wilderness experience.""",
        "highlights": [
            "A dramatic glacier amphitheatre with snow-capped walls",
            "Steep & challenging ascent through varied terrain",
            "Proximity to Pahalgam - perfect for a quick adventure",
            'Baisaran meadows known as "Mini Switzerland of India"',
            "Glacier-fed crystal clear lake surrounded by permanent snow"
        ]
    },
    "gangbal-nandkol-trek.html": {
        "history": """Gangbal has been a sacred pilgrimage lake for Kashmiri Pandits for centuries, considered the abode of
                    Lord Shiva. The trail through Naranag was once a vital trade path linking Kashmir with Harmukh's
                    northern tribes. The ancient Naranag temple ruins at the base add historical significance to this
                    spiritual trek.""",
        "highlights": [
            "Twin alpine lakes - Gangbal and Nandkol - of spiritual significance",
            'Stunning views of Mount Harmukh (5,142 m), the "Kailash of Kashmir"',
            "Short yet rewarding trek perfect for beginners",
            "Ancient Naranag temple complex dating back to 8th century",
            "Crystal clear waters reflecting the majestic Harmukh peak"
        ]
    },
    "kousarnag-trek.html": {
        "history": """One of Kashmir's largest glacier lakes, Kousarnag is mentioned in several ancient Hindu texts and
                    local folklore. The lake has been visited by locals for centuries during seasonal migrations. The
                    trek starts from the spectacular Aharbal waterfall, known as the "Niagara of Kashmir," adding to the
                    trek's unique character.""",
        "highlights": [
            "Massive glacier-fed lake - one of Kashmir's largest",
            "Remote & untouched environment with minimal crowds",
            'Trekking via Aharbal waterfall, the "Niagara of Kashmir"',
            "Rich mythology and spiritual significance",
            "Vast glacial basin surrounded by towering peaks"
        ]
    },
    "sheshnag-lake-trek.html": {
        "history": """Part of the historic Amarnath Yatra pilgrimage route, Sheshnag Lake derives its name from the
                    mythical serpent god Sheshnag. The lake has been a spiritual rest point for pilgrims for thousands
                    of years. According to legend, the lake is named after the seven-headed serpent that Lord Shiva
                    wears around his neck.""",
        "highlights": [
            "Religious and spiritual significance on the Amarnath Yatra route",
            "Easy access from Pahalgam",
            "Bright green alpine lake surrounded by snow peaks",
            "Perfect for beginner trekkers and families",
            "Well-established trail with good infrastructure"
        ]
    },
    "bandipora-gangbal-trek.html": {
        "history": """This alternative route to Gangbal Lake via Bandipora offers a different perspective of the sacred twin lakes.
                    The trail passes through dense forests and remote villages, providing insights into the traditional lifestyle
                    of Kashmiri mountain communities. This route is less traveled compared to the Naranag route, offering more
                    solitude and wilderness experience.""",
        "highlights": [
            "Alternative route to the sacred Gangbal Lake",
            "Less crowded than the Naranag route",
            "Passes through traditional Kashmiri villages",
            "Dense forests and diverse wildlife",
            "Views of Mount Harmukh from a different angle"
        ]
    },
    "kolahoi-glacier-trek.html": {
        "history": """Kolahoi Peak (5,425 m), often called the "Matterhorn of Kashmir," has drawn explorers since the
                    British era. Treks to the glacier became famous in the 1930s when mountaineers first documented the
                    region. The glacier feeds the Lidder River and is a major source of water for the Kashmir valley.""",
        "highlights": [
            "Dramatic glacier viewpoint below the majestic Kolahoi Peak",
            "Pahalgam's most iconic and challenging trek",
            "Rugged terrain with boulders, moraines & ice formations",
            "Source of the Lidder River",
            'Stunning views of the "Matterhorn of Kashmir"'
        ]
    }
}

def add_overview_tab(filename, data):
    """Add Overview tab content to trek page"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if Overview tab already exists
        if 'id="overview"' in content:
            print(f"[SKIP] {filename} already has Overview tab")
            return True
        
        # Create the Overview tab HTML
        highlights_html = '\n'.join([f'                    <li>{h}</li>' for h in data["highlights"]])
        
        overview_section = f'''
            <!-- Tab: Overview -->
            <div id="overview" class="detail-tab-content active">
                <h2>Brief History</h2>
                <p style="line-height: 1.8; margin-bottom: 20px; color: #ccc;">
                    {data["history"]}
                </p>
                <h3>What It Is Famous For</h3>
                <ul style="list-style: disc; margin-left: 20px; color: #ccc; line-height: 1.8;">
{highlights_html}
                </ul>

                <!-- Route Map (Mobile Only) -->
                <div class="mobile-only-content">
                    <h3 style="margin-top: 30px;">Route Map</h3>
                    <div
                        style="background: #333; height: 150px; display: flex; align-items: center; justify-content: center; color: #888; border-radius: 8px; margin-top: 15px;">
                        [Map Placeholder]
                    </div>
                </div>

                <!-- Altitude Profile (Mobile Only) -->
                <div class="mobile-only-content">
                    <h3 style="margin-top: 30px;">Altitude Profile</h3>
                    <div
                        style="background: #333; height: 150px; display: flex; align-items: center; justify-content: center; color: #888; border-radius: 8px; margin-top: 15px;">
                        [Altitude Chart Placeholder]
                    </div>
                </div>
            </div>
'''
        
        # Find the position to insert (before the Itinerary tab)
        itinerary_pattern = r'(\s*<!-- Tab: Itinerary -->)'
        
        if re.search(itinerary_pattern, content):
            # Insert Overview section before Itinerary
            content = re.sub(
                itinerary_pattern,
                overview_section + r'\n\1',
                content,
                count=1
            )
            
            # Write updated content
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"[SUCCESS] Added Overview tab to {filename}")
            return True
        else:
            print(f"[ERROR] Could not find insertion point in {filename}")
            return False
        
    except Exception as e:
        print(f"[ERROR] Error updating {filename}: {str(e)}")
        return False

# Add Overview tabs to all trek files
print("Adding Overview tabs to trek pages...\n")
success_count = 0
for filename, data in overview_data.items():
    if add_overview_tab(filename, data):
        success_count += 1

print(f"\n{'='*50}")
print(f"Update Complete: {success_count}/{len(overview_data)} files updated successfully")
print(f"{'='*50}")
