import re

# Trek data extracted from kashmir-treks-guide.html
trek_data = {
    "tulian-lake-trek.html": {
        "title": "Tulian Lake Trek",
        "meta_desc": "Experience the Tulian Lake Trek - 4 days through dramatic glacier amphitheater, Baisaran meadows, and pristine alpine lake near Pahalgam, Kashmir.",
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
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and preparation."),
            ("Day 2: Srinagar → Pahalgam → Baisaran → Tulian Valley (8 km trek)", 
             'Drive to Pahalgam. Trek through Baisaran meadows ("Mini Switzerland") with panoramic mountain views. Camp in Tulian Valley.'),
            ("Day 3: Tulian Valley → Tulian Lake → Return to Camp (6 km)", 
             "Steep ascent to reach the glacier-fed lake surrounded by snow-capped walls. Explore the amphitheater and return to camp."),
            ("Day 4: Descend to Pahalgam → Srinagar", "Descend through meadows, drive back to Srinagar.")
        ]
    },
    "gangbal-nandkol-trek.html": {
        "title": "Gangbal-Nandkol Trek",
        "meta_desc": "Sacred Gangbal-Nandkol Trek - 4 days to twin alpine lakes below Mount Harmukh, ancient Naranag temples, spiritual journey in Kashmir.",
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
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and trek preparation."),
            ("Day 2: Srinagar → Naranag → Trunkhol (10 km trek)", 
             "Drive to Naranag. Visit ancient temple ruins. Long forest climb through pine and fir forests into meadows. Camp at Trunkhol."),
            ("Day 3: Trunkhol → Gangbal & Nandkol (7 km)", 
             "Ascend to reach the beautiful twin lakes situated under the towering Harmukh peak. Camp beside the sacred waters."),
            ("Day 4: Gangbal → Naranag → Srinagar", "Descend to Naranag, drive back to Srinagar.")
        ]
    },
    "kousarnag-trek.html": {
        "title": "Kousarnag Lake Trek",
        "meta_desc": "Kousarnag Lake Trek - 5 days to sacred healing lake, remote alpine meadows, spiritual pilgrimage trek in Kashmir Himalayas.",
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
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and preparation."),
            ("Day 2: Srinagar → Aharbal → Kongwattan (12 km trek)", 
             "Drive to Aharbal waterfall. Begin trek through forests and meadows. Camp at Kongwattan."),
            ("Day 3: Kongwattan → Kousarnag Lake (8 km)", 
             "Gradual ascent to reach the vast glacial basin and the magnificent Kousarnag lake. Camp beside the lake."),
            ("Day 4: Explore → Return to Kongwattan", "Exploration day around the lake, then return to Kongwattan camp."),
            ("Day 5: Kongwattan → Aharbal → Srinagar", "Descend to Aharbal, drive back to Srinagar.")
        ]
    },
    "sheshnag-lake-trek.html": {
        "title": "Sheshnag Lake Trek",
        "meta_desc": "Sheshnag Lake Trek - 3 days on the Amarnath Yatra route, easy alpine trek to sacred lake in Kashmir.",
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
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and preparation."),
            ("Day 2: Srinagar → Pahalgam → Chandanwari → Sheshnag (13 km trek)", 
             "Drive to Chandanwari. Trek along the Amarnath Yatra route to reach the sacred Sheshnag Lake. Camp beside the lake."),
            ("Day 3: Sheshnag → Chandanwari → Pahalgam → Srinagar", "Descend to Chandanwari, drive back to Srinagar.")
        ]
    },
    "bandipora-gangbal-trek.html": {
        "title": "Bandipora-Gangbal Trek",
        "meta_desc": "Bandipora-Gangbal Trek - 5 days alternative route to sacred lakes, remote villages, less crowded Kashmir trek.",
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
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and preparation."),
            ("Day 2: Srinagar → Bandipora → Trek Start", "Drive to Bandipora. Begin trek through forests."),
            ("Day 3: Forest trek to Trunkhol", "Long forest climb through pine and fir forests into meadows. Camp at Trunkhol."),
            ("Day 4: Trunkhol → Gangbal & Nandkol", "Ascend to reach the beautiful twin lakes. Camp beside the sacred waters."),
            ("Day 5: Gangbal → Naranag → Srinagar", "Descend via Naranag route, drive back to Srinagar.")
        ]
    },
    "kolahoi-glacier-trek.html": {
        "title": "Kolahoi Glacier Trek",
        "meta_desc": "Kolahoi Glacier Trek - 4 days to the Matterhorn of Kashmir, dramatic glacier views, challenging Pahalgam trek.",
        "history": """Kolahoi Peak (5,425 m), often called the "Matterhorn of Kashmir," has drawn explorers since the
                    British era. Treks to the glacier became famous in the 1930s when mountaineers first documented the
                    region. The glacier feeds the Lidder River and is a major source of water for the Kashmir valley.""",
        "highlights": [
            "Dramatic glacier viewpoint below the majestic Kolahoi Peak",
            "Pahalgam's most iconic and challenging trek",
            "Rugged terrain with boulders, moraines & ice formations",
            "Source of the Lidder River",
            'Stunning views of the "Matterhorn of Kashmir"'
        ],
        "itinerary": [
            ("Day 1: Arrive in Srinagar", "Check-in and preparation."),
            ("Day 2: Srinagar → Aru → Lidderwat (11 km trek)", 
             "Drive to Aru. Trek through pine forests to Lidderwat meadows."),
            ("Day 3: Lidderwat → Satlanjan → Kolahoi Glacier View → Return (14 km)", 
             "Long day trek through boulder fields and moraines to reach the glacier viewpoint. Spectacular views of Kolahoi Peak. Return to Lidderwat camp."),
            ("Day 4: Lidderwat → Aru → Srinagar", "Descend to Aru, drive back to Srinagar.")
        ]
    }
}

def update_trek_file(filename, data):
    """Update a trek HTML file with complete content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update meta description
        content = re.sub(
            r'<meta name="description"\s+content="[^"]*"',
            f'<meta name="description"\n        content="{data["meta_desc"]}"',
            content
        )
        
        # Update Brief History section
        history_pattern = r'(<h2>Brief History</h2>\s*<p[^>]*>)(.*?)(</p>)'
        content = re.sub(
            history_pattern,
            rf'\1{data["history"]}\3',
            content,
            flags=re.DOTALL
        )
        
        # Update Highlights section
        highlights_html = '\n'.join([f'                    <li>{h}</li>' for h in data["highlights"]])
        highlights_pattern = r'(<h3>What It Is Famous For</h3>\s*<ul[^>]*>)(.*?)(</ul>)'
        content = re.sub(
            highlights_pattern,
            rf'\1\n{highlights_html}\n                \3',
            content,
            flags=re.DOTALL
        )
        
        # Update Itinerary section
        itinerary_html = '\n'.join([
            f'''                <div class="itinerary-step">
                    <h3>{day}</h3>
                    <p>{desc}</p>
                </div>'''
            for day, desc in data["itinerary"]
        ])
        
        itinerary_pattern = r'(<h2>Day-by-Day Itinerary</h2>\s*<br>\s*)(.*?)(\s*</div>\s*\n\s*<!-- Tab: Inclusions -->)'
        content = re.sub(
            itinerary_pattern,
            rf'\1\n{itinerary_html}\n            \3',
            content,
            flags=re.DOTALL
        )
        
        # Write updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[SUCCESS] Successfully updated {filename}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error updating {filename}: {str(e)}")
        return False

# Update all trek files
print("Starting trek page updates...\n")
success_count = 0
for filename, data in trek_data.items():
    if update_trek_file(filename, data):
        success_count += 1

print(f"\n{'='*50}")
print(f"Update Complete: {success_count}/{len(trek_data)} files updated successfully")
print(f"{'='*50}")
