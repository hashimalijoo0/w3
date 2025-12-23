$files = Get-ChildItem -Path "c:\Users\hashi\w3\*.html"
$newRegistration = @'
    <div class="footer-registration">
        <div class="registration-content">
            <h3>Snowman Adventures is Officially Registered with</h3>
            <div class="registration-logos">
                <div class="reg-logo-item">
                    <div class="reg-circle">JK Tour</div>
                    <span>JK Tourism</span>
                </div>
                <div class="reg-logo-item">
                    <div class="reg-circle">ATOI</div>
                    <span>ATOI</span>
                </div>
                <div class="reg-logo-item">
                    <div class="reg-circle">ATOAK</div>
                    <span>ATOAK</span>
                </div>
            </div>
        </div>
    </div>
'@

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # 1. Remove Blog link from navigation (usually <li><a href="blog.html">Blog</a></li>)
    $content = $content -replace '<li><a href="blog.html">Blog</a></li>', ''
    $content = $content -replace '<li><a href="blog.html" class="active">Blog</a></li>', ''
    $content = $content -replace '<li><a href="blog.html">BLOG</a></li>', ''
    $content = $content -replace '<li><a href="blog.html" class="active">BLOG</a></li>', ''
    
    # 2. Remove Blog link from footer (sometimes different format)
    $content = $content -replace '<li><a href="blog.html"[^>]*>Blog</a></li>', ''
    
    # 3. Handle registration section
    if ($file.Name -eq "index.html") {
        # Ensure index.html has the updated registration section
        # Replace existing registration section with the new one
        if ($content -match '(?s)<div class="footer-registration">.*?</div>\s+</div>') {
            $content = $content -replace '(?s)<div class="footer-registration">.*?</div>\s+</div>', ("$newRegistration`r`n    </div>")
        }
        elseif ($content -match '(?s)<div class="footer-registration">.*?</div>') {
            $content = $content -replace '(?s)<div class="footer-registration">.*?</div>', $newRegistration
        }
    }
    else {
        # Remove registration section from all other pages
        # Look for the registration div and remove it along with its following whitespace up to the next prominent element
        $content = $content -replace '(?s)<!-- Registration Banner -->.*?<div class="footer-registration">.*?</div>\s*', ''
        $content = $content -replace '(?s)<div class="footer-registration">.*?</div>\s*', ''
    }
    
    Set-Content $file.FullName $content -Encoding UTF8
}

Write-Host "Deleting blog.html..."
if (Test-Path "c:\Users\hashi\w3\blog.html") {
    Remove-Item "c:\Users\hashi\w3\blog.html"
}

Write-Host "Done!"
