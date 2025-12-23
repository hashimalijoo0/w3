$newFooter = @'
<footer>
    <!-- Registration Banner -->
    <div class="footer-registration">
        <div class="registration-content">
            <img src="assets/logo.jpg" alt="Snowman Adventures Logo" class="registration-logo">
            <h3>Snowman Adventures is Officially Registered with JK Tourism, ATOAK, ATOI</h3>
            <p>Explore the untold beauty of Kashmir with expert guides and premium equipment.</p>
        </div>
    </div>

    <!-- Main Footer -->
    <div class="footer-main">
        <div class="footer-container">
            <!-- Quick Links -->
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="adventures.html">Upcoming Adventures</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms & Conditions</a></li>
                </ul>
            </div>

            <!-- Follow Us On -->
            <div class="footer-col">
                <h3>Follow Us On</h3>
                <div class="social-links">
                    <a href="https://wa.me/+919622494350" target="_blank"><i class="fab fa-whatsapp"></i></a>
                    <a href="https://www.instagram.com/snowmanadventuress/" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="#" target="_blank"><i class="fab fa-youtube"></i></a>
                </div>
            </div>

            <!-- Contact Us -->
            <div class="footer-col">
                <h3>Contact Us</h3>
                <div class="contact-info">
                    <p><i class="fas fa-phone"></i> +91 96224 94350</p>
                    <p><i class="far fa-clock"></i> Mon to Sun - 9.00 AM to 9.00 PM</p>
                    <p><strong>Office:</strong> Srinagar, Kashmir</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer Bottom -->
    <div class="footer-bottom">
        <div class="footer-container">
            <p>&copy; 2024 Snowman Adventures. All rights reserved.</p>
            <p>All images are copyrighted by their respective authors.</p>
        </div>
    </div>
</footer>
'@

$cssFile = "c:\Users\hashi\w3\css\style.css"
$cssContent = Get-Content $cssFile -Raw
$newCss = @'
/* ===================================
   FOOTER - Modern & Premium Design
   =================================== */
footer {
    background-color: #fff;
    color: #333;
    padding: 0;
    margin-top: 60px;
    border-top: 1px solid #eee;
    font-family: 'Inter', sans-serif;
}

.footer-registration {
    background-color: #fffbeb; /* Light creamy background */
    padding: 30px 20px;
    text-align: center;
    border-bottom: 1px solid #fef3c7;
}

.registration-content {
    max-width: 1200px;
    margin: 0 auto;
}

.registration-logo {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-bottom: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.registration-content h3 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 10px;
}

.registration-content p {
    font-size: 0.95rem;
    color: #666;
}

.footer-main {
    padding: 60px 20px;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
}

.footer-col h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 25px;
    position: relative;
}

.footer-col ul {
    list-style: none;
    padding: 0;
}

.footer-col ul li {
    margin-bottom: 12px;
}

.footer-col ul li a {
    color: #444;
    font-size: 0.95rem;
    transition: color 0.3s;
}

.footer-col ul li a:hover {
    color: var(--accent-color);
}

.social-links {
    display: flex;
    gap: 15px;
}

.social-links a {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f8f9fa;
    border-radius: 50%;
    color: #333;
    font-size: 1.2rem;
    transition: all 0.3s ease;
    border: 1px solid #eee;
}

.social-links a:hover {
    background: var(--accent-color);
    color: #fff;
    transform: translateY(-3px);
    border-color: var(--accent-color);
}

.contact-info p {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 15px;
    font-size: 0.95rem;
    color: #444;
}

.contact-info p i {
    color: #666;
    width: 20px;
}

.footer-bottom {
    background-color: #fff;
    padding: 25px 20px;
    border-top: 1px solid #eee;
}

.footer-bottom .footer-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
    color: #888;
}

/* Response for Footer */
@media (max-width: 768px) {
    .footer-container {
        grid-template-columns: 1fr;
        gap: 30px;
        text-align: center;
    }

    .social-links {
        justify-content: center;
    }

    .contact-info p {
        justify-content: center;
    }

    .footer-bottom .footer-container {
        flex-direction: column;
        gap: 10px;
    }
}
'@

# Update CSS
$regex = "(?s)/\* ===================================\s+FOOTER - Modern & Attractive Design.*?.footer-bottom p \{.*?\}"
$updatedCss = $cssContent -replace $regex, $newCss
Set-Content $cssFile $updatedCss -Encoding UTF8

# Update HTML files
$files = Get-ChildItem -Path "c:\Users\hashi\w3\*.html"
foreach ($file in $files) {
    Write-Host "Updating $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    $updatedContent = $content -replace "(?s)<footer>.*?</footer>", $newFooter
    Set-Content $file.FullName $updatedContent -Encoding UTF8
}
Write-Host "Done!"
