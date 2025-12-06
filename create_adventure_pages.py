
import os

base_dir = "c:\\Users\\hashi\\w3"

# Common Header/Footer content (simplified for injection)
header_html = """
    <header>
        <a href="index.html" class="brand-container">
            <img src="assets/logo.jpg" alt="Snowman Adventures Logo" class="hero-logo">
            <span class="brand-text">Snowman Adventures</span>
        </a>
        <nav>
            <div class="burger-menu">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="adventures.html">Adventures</a></li>
                <li><a href="tour-packages.html">Tour Packages</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>
"""

footer_html = """
    <footer>
        <div class="footer-content">
            <div class="footer-logo">
                <div class="footer-brand-section">
                    <img src="assets/logo.jpg" alt="Snowman Adventures" class="footer-logo-img">
                    <span class="footer-company-name">Snowman Adventures</span>
                </div>
                <p class="footer-tagline">Experience the untold beauty of Kashmir with expert guides and premium equipment.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <div class="footer-links">
                    <a href="index.html">Home</a>
                    <a href="adventures.html">Adventures</a>
                    <a href="tour-packages.html">Tour Packages</a>
                    <a href="about.html">About Us</a>
                    <a href="contact.html">Contact</a>
                </div>
            </div>
            <div class="footer-section">
                <h3>Connect With Us</h3>
                <div class="social-icons">
                    <a href="https://wa.me/+919622494350" target="_blank" class="social-icon"><i class="fab fa-whatsapp"></i></a>
                    <a href="#" target="_blank" class="social-icon"><i class="fab fa-youtube"></i></a>
                    <a href="#" target="_blank" class="social-icon"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 Snowman Adventures. All rights reserved.</p>
        </div>
    </footer>
    <script src="js/main.js"></script>
"""

def create_page(filename, title, hero_img, location, content_html):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Snowman Adventures</title>
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap" rel="stylesheet">
    <link rel="icon" href="assets/logo.jpg" type="image/jpeg">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .detail-hero {{
            height: 60vh;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.6)), url('{hero_img}');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding-top: 80px;
        }}
        .detail-hero h1 {{ font-size: 3.5rem; margin-bottom: 20px; text-transform: uppercase; text-shadow: 2px 2px 5px black; }}
        .location-badge {{ font-size: 1.5rem; background: rgba(0,0,0,0.6); padding: 10px 25px; border-radius: 50px; border: 1px solid var(--accent-color); }}
        .content-section {{ max-width: 1000px; margin: 0 auto; padding: 60px 20px; text-align: center; }}
        .content-section h2 {{ font-size: 2.5rem; margin-bottom: 30px; }}
        .content-section p {{ color: #ccc; font-size: 1.1rem; line-height: 1.8; margin-bottom: 40px; }}
    </style>
</head>
<body>
    {header_html}

    <div class="detail-hero">
        <h1>{title}</h1>
        {"<div class='location-badge'><i class='fas fa-map-marker-alt'></i> " + location + "</div>" if location else ""}
    </div>

    <div class="content-section">
        {content_html}
    </div>

    {footer_html}
</body>
</html>
"""
    with open(os.path.join(base_dir, filename), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {filename}")

# 1. Rafting
rafting_content = """
    <h2>White Water Rafting in Pahalgam</h2>
    <p>Experience the thrill of navigating the gushing Lidder River in Pahalgam. Whether you are a beginner or an adventure enthusiast, our rafting rides offer an exhilarating experience amidst breathtaking scenery.</p>
    
    <div class="pricing-grid" style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
        <!-- Short Ride -->
        <div class="pricing-card" style="min-width: 300px; padding: 30px; background: #1a1a1a; border-radius: 10px; border: 1px solid #333;">
            <h3 style="color: white; margin-bottom: 10px;">Short Ride</h3>
            <div class="price-tag" style="font-size: 2rem; color: var(--accent-color); font-weight: bold; margin-bottom: 20px;">₹800 <span style="font-size: 1rem; color: #888;">/ person</span></div>
            <ul class="features-list" style="text-align: left; margin-bottom: 25px; color: #ccc; list-style: none;">
                <li style="margin-bottom: 10px;">✅ 2.5 km stretch</li>
                <li style="margin-bottom: 10px;">✅ Duration: ~30 mins</li>
                <li style="margin-bottom: 10px;">✅ Difficulty: Easy/Moderate</li>
            </ul>
            <a href="https://wa.me/919622494350?text=I'm interested in Rafting Short Ride" class="btn" style="display: block; width: 100%; text-align: center;">Book Short Ride</a>
        </div>

        <!-- Long Ride -->
        <div class="pricing-card featured" style="min-width: 300px; padding: 30px; background: #1a1a1a; border-radius: 10px; border: 1px solid var(--accent-color); transform: scale(1.05);">
            <div style="background: var(--accent-color); color: white; display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; margin-bottom: 15px;">POPULAR</div>
            <h3 style="color: white; margin-bottom: 10px;">Long Ride</h3>
            <div class="price-tag" style="font-size: 2rem; color: var(--accent-color); font-weight: bold; margin-bottom: 20px;">₹1,200 <span style="font-size: 1rem; color: #888;">/ person</span></div>
            <ul class="features-list" style="text-align: left; margin-bottom: 25px; color: #ccc; list-style: none;">
                <li style="margin-bottom: 10px;">✅ 5-7 km stretch</li>
                <li style="margin-bottom: 10px;">✅ Duration: ~1 hour</li>
                <li style="margin-bottom: 10px;">✅ Difficulty: Moderate (Rapid Grades II & III)</li>
            </ul>
            <a href="https://wa.me/919622494350?text=I'm interested in Rafting Long Ride" class="btn" style="display: block; width: 100%; text-align: center;">Book Long Ride</a>
        </div>
    </div>
"""
create_page("rafting.html", "Rafting", "https://images.pexels.com/photos/2398220/pexels-photo-2398220.jpeg", "Yenner, Pahalgam", rafting_content)


# 2. Paragliding
paragliding_content = """
    <h2>Paragliding in Dara</h2>
    <p>Soar high above the Zabarwan range and witness the majestic Dal Lake from the sky. Our paragliding flights from Dara offer an unmatched bird's eye view of Srinagar valley.</p>
    
    <div class="pricing-grid" style="display: flex; justify-content: center; gap: 30px; margin-top: 40px;">
        <div class="pricing-card featured" style="max-width: 400px; padding: 40px; background: #1a1a1a; border-radius: 10px; border: 1px solid var(--accent-color);">
            <h3 style="color: white; margin-bottom: 10px;">Standard Flight</h3>
            <div class="price-tag" style="font-size: 2.5rem; color: var(--accent-color); font-weight: bold; margin-bottom: 20px;">₹2,000 <span style="font-size: 1rem; color: #888;">/ person</span></div>
            <ul class="features-list" style="text-align: left; margin-bottom: 25px; color: #ccc; list-style: none;">
                <li style="margin-bottom: 10px;">✅ Flight Duration: 15-20 mins</li>
                <li style="margin-bottom: 10px;">✅ GoProm Video Included</li>
                <li style="margin-bottom: 10px;">✅ Expert Pilot</li>
                <li style="margin-bottom: 10px;">✅ Transport to Take-off Point</li>
            </ul>
            <a href="https://wa.me/919622494350?text=I'm interested in Paragliding at Dara" class="btn" style="display: block; width: 100%; text-align: center;">Book Now</a>
        </div>
    </div>
"""
create_page("paragliding.html", "Paragliding", "https://images.pexels.com/photos/1666021/pexels-photo-1666021.jpeg", "Dara, Srinagar", paragliding_content)


# 3. Water Skiing (Coming Soon)
coming_soon = """
    <h2 style="font-size: 3rem; color: #888;">COMING SOON</h2>
    <p>We are currently setting up this adventure experience. Stay tuned!</p>
    <a href="contact.html" class="btn">Contact for Updates</a>
"""
create_page("water-skiing.html", "Water Skiing", "https://images.pexels.com/photos/416676/pexels-photo-416676.jpeg", "", coming_soon)

# 4. Ice Climbing (Coming Soon)
create_page("ice-climbing.html", "Ice Climbing", "https://images.pexels.com/photos/869258/pexels-photo-869258.jpeg", "", coming_soon)


# 5. Update Adventures.html Links
adventures_path = os.path.join(base_dir, "adventures.html")
with open(adventures_path, 'r', encoding='utf-8') as f:
    adv_content = f.read()

# Replace links
replacements = {
    'adventure-detail.html?name=Rafting': 'rafting.html',
    'adventure-detail.html?name=Paragliding': 'paragliding.html',
    'adventure-detail.html?name=Water%20Skiing': 'water-skiing.html',
    'adventure-detail.html?name=Ice%20Climbing': 'ice-climbing.html'
}

new_adv_content = adv_content
for old, new in replacements.items():
    new_adv_content = new_adv_content.replace(old, new)

if new_adv_content != adv_content:
    with open(adventures_path, 'w', encoding='utf-8') as f:
        f.write(new_adv_content)
    print("Updated adventures.html links.")
else:
    print("No links updated in adventures.html (already updated?).")
