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

$files = Get-ChildItem -Path "c:\Users\hashi\w3\*.html"
foreach ($file in $files) {
    Write-Host "Updating registration section in $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    $updatedContent = $content -replace "(?s)<div class=""footer-registration"">.*?</div>\s+</div>", "$newRegistration`r`n    </div>"
    # The above regex might be tricky due to nesting. Let's try a safer approach:
    # Replace the whole registration div block.
    $updatedContent = $content -replace "(?s)<div class=""footer-registration"">.*?</div>\s+</div>", ($newRegistration + "`r`n")
    # Actually, simpler: replace based on the existing content structure
    $regex = "(?s)<div class=""footer-registration"">.*?</div>\s+<!-- Main Footer -->"
    if ($content -match $regex) {
        $updatedContent = $content -replace $regex, ("$newRegistration`r`n`r`n    <!-- Main Footer -->")
        Set-Content $file.FullName $updatedContent -Encoding UTF8
    }
    else {
        Write-Host "Pattern not found in $($file.Name)"
    }
}
Write-Host "Done!"
