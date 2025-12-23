$cssFile = "c:\Users\hashi\w3\css\style.css"
$cssContent = Get-Content $cssFile -Raw

$newCss = @'
/* ===================================
   FOOTER - Modern & Premium Design
   =================================== */
footer {
    background-color: #000;
    color: var(--text-color);
    padding: 0;
    margin-top: 60px;
    border-top: 1px solid #1a1a1a;
    font-family: 'Inter', sans-serif;
}

.footer-registration {
    background-color: #0a0a0a; /* Dark background matching the page */
    padding: 40px 20px;
    text-align: center;
    border-bottom: 1px solid #1a1a1a;
    position: relative;
}

.footer-registration::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 2px;
    background: var(--accent-color);
}

.registration-content {
    max-width: 1200px;
    margin: 0 auto;
}

.registration-logo {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(231, 76, 60, 0.2);
    border: 2px solid var(--accent-color);
}

.registration-content h3 {
    font-size: 1.6rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.registration-content p {
    font-size: 1rem;
    color: var(--secondary-text);
}

.footer-main {
    padding: 70px 20px;
    background-color: #000;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 50px;
}

.footer-col h3 {
    font-size: 1.25rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 30px;
    position: relative;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.footer-col h3::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 40px;
    height: 2px;
    background: var(--accent-color);
}

.footer-col ul {
    list-style: none;
    padding: 0;
}

.footer-col ul li {
    margin-bottom: 15px;
}

.footer-col ul li a {
    color: var(--secondary-text);
    font-size: 1rem;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;
}

.footer-col ul li a:hover {
    color: var(--accent-color);
    transform: translateX(5px);
}

.social-links {
    display: flex;
    gap: 20px;
}

.social-links a {
    width: 45px;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #111;
    border-radius: 50%;
    color: #fff;
    font-size: 1.3rem;
    transition: all 0.3s ease;
    border: 1px solid #222;
}

.social-links a:hover {
    background: var(--accent-color);
    color: #fff;
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 5px 15px rgba(231, 76, 60, 0.4);
}

.contact-info p {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    font-size: 1rem;
    color: var(--secondary-text);
}

.contact-info p i {
    color: var(--accent-color);
    width: 20px;
}

.footer-bottom {
    background-color: #000;
    padding: 30px 20px;
    border-top: 1px solid #1a1a1a;
}

.footer-bottom .footer-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.9rem;
    color: #666;
}

/* Response for Footer */
@media (max-width: 768px) {
    .footer-container {
        grid-template-columns: 1fr;
        gap: 40px;
        text-align: center;
    }

    .footer-col h3::after {
        left: 50%;
        transform: translateX(-50%);
    }

    .footer-col ul li a {
        justify-content: center;
    }

    .social-links {
        justify-content: center;
    }

    .contact-info p {
        justify-content: center;
    }

    .footer-bottom .footer-container {
        flex-direction: column;
        gap: 15px;
    }
}
'@

# Update CSS with robust regex
$startMarker = "/\* ===================================\s+FOOTER - Modern & Premium Design.*?\*/"
$endMarker = "/\* --- WhatsApp Float Button --- \*/"

# Escape markers for regex
$regex = "(?s)" + [regex]::Escape("/* ===================================") + ".*?" + [regex]::Escape("/* --- WhatsApp Float Button --- */")
$fullNewCss = $newCss + "`r`n`r`n/* --- WhatsApp Float Button --- */"

$updatedCss = $cssContent -replace $regex, $fullNewCss

# Fallback if first regex fails (trying Attractive Design marker just in case)
if ($updatedCss -eq $cssContent) {
    $regex2 = "(?s)" + [regex]::Escape("/* ===================================") + ".*?" + [regex]::Escape("FOOTER - Modern & Attractive Design") + ".*?" + [regex]::Escape("/* --- WhatsApp Float Button --- */")
    $updatedCss = $cssContent -replace $regex2, $fullNewCss
}

Set-Content $cssFile $updatedCss -Encoding UTF8
Write-Host "CSS Update Complete!"
