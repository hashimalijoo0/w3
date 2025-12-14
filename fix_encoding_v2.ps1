$files = Get-ChildItem "c:\Users\hashi\w3\*.html" -Recurse

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding utf8
    $newContent = $content -replace "â‚¹", "&#8377;" `
        -replace "âœ…", "&#9989;" `
        -replace "â€™", "'" `
        -replace "â€”", " - " `
                           -replace "â†’", "&#8594;" `
                           -replace "â–¼", "&#9660;" `
                           -replace "â€¢", "&bull;" `
                           -replace "â Œ", "&#10060;" `
                           -replace "â€“", "-"
    
    if ($content -ne $newContent) {
        Write-Host "Updating $($file.Name)"
        $newContent | Set-Content $file.FullName -Encoding utf8
    }
}
