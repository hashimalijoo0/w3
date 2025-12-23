$files = Get-ChildItem -Path "c:\Users\hashi\w3\*.html"
foreach ($file in $files) {
    if ($file.Name -eq "index.html") { continue }
    
    Write-Host "Cleaning up $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # Target the mangled registration section precisely
    $regex = '(?s)<footer>\s+<span>JK Tourism</span>.*?</div>\s+</div>\s+</div>\s+<!-- Main Footer -->'
    if ($content -match $regex) {
        $content = $content -replace $regex, "<footer>`r`n`r`n    <!-- Main Footer -->"
    }
    else {
        # Fallback for slightly different mangling
        $regex2 = '(?s)<footer>\s+<!-- Registration Banner -->.*?</div>\s+</div>\s+<!-- Main Footer -->'
        $content = $content -replace $regex2, "<footer>`r`n`r`n    <!-- Main Footer -->"
        
        # Even broader fallback
        $regex3 = '(?s)<footer>\s+<div class="footer-registration">.*?</div>\s+<!-- Main Footer -->'
        $content = $content -replace $regex3, "<footer>`r`n`r`n    <!-- Main Footer -->"
    }
    
    # Let's also make sure there are no double footers or weirdness
    Set-Content $file.FullName $content -Encoding UTF8
}
Write-Host "Cleanup done!"
