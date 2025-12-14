$replacements = @{
    'â–¼' = '&#9660;'
    'â†’' = '&#8594;'
    'âœ…' = '&#9989;'
    'âŒ' = '&#10060;'
    'â‚¹' = '&#8377;'
    'â€“' = '&ndash;'
    'â€”' = '&mdash;'
    'â€œ' = '&ldquo;'
    'â€' = '&rdquo;'
    'â€™' = '&rsquo;'
    'â€¢' = '&bull;'
}

Get-ChildItem * .html | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $modified = $false
    foreach ($key in $replacements.Keys) {
        if ($content.Contains($key)) {
            $content = $content.Replace($key, $replacements[$key])
            $modified = $true
        }
    }
    if ($modified) {
        Set-Content -Path $_.FullName -Value $content -Encoding utf8
        Write-Host "Fixed encoding in $($_.Name)"
    }
}
