$newFooterMain = @'
    <footer>
        <div class="footer-main">
            <div class="footer-container">
                <!-- Quick Links -->
                <div class="footer-col">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="tour-packages.html">Tour Packages</a></li>
                        <li><a href="solo-self-drive-support.html">Solo Support</a></li>
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms & Conditions</a></li>
                    </ul>
                </div>

                <!-- Follow Us On -->
                <div class="footer-col">
                    <h3>Follow Us On</h3>
                    <div class="social-links">
                        <a href="https://wa.me/+919622494350" target="_blank"><i class="fab fa-whatsapp"></i></a>
                        <a href="https://www.instagram.com/snowmanadventuress/" target="_blank"><i
                                class="fab fa-instagram"></i></a>
                        <a href="#" target="_blank"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>

                <!-- Contact Us -->
                <div class="footer-col">
                    <h3>Contact Us</h3>
                    <div class="contact-info">
                        <p><i class="fas fa-phone"></i> +91 97977 98424</p>
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

$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    if ($file.Name -eq "index.html") {
        # Index has a registration section above the main footer, only update footer-main onwards
        $content = Get-Content $file.FullName -Raw
        $regex = '(?s)<div class="footer-main">.*?</footer>'
        $newIndexFooter = $newFooterMain -replace '(?s).*?<div class="footer-main">', '<div class="footer-main">'
        $updatedContent = $content -replace $regex, $newIndexFooter
        Set-Content $file.FullName $updatedContent
        Write-Host "Updated index.html (Main Footer part)"
    }
    else {
        # Other pages replace entire <footer> block
        $content = Get-Content $file.FullName -Raw
        $regex = '(?s)<footer>.*?</footer>'
        $updatedContent = $content -replace $regex, $newFooterMain
        Set-Content $file.FullName $updatedContent
        Write-Host "Updated $($file.Name)"
    }
}
