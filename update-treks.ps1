# Update Tulian Lake Trek
$content = Get-Content 'tulian-lake-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Tulian Lake Trek'
$content = $content -replace '8 Days', '4 Days'
$content = $content -replace '13,800 ft', '12,800 ft'
$content = $content -replace 'Moderate to Challenging', 'Moderate to Challenging'
$content = $content -replace 'Jul-Sep', 'Jun-Oct'
$content | Set-Content 'tulian-lake-trek.html'

# Update Gangbal-Nandkol Trek  
$content = Get-Content 'gangbal-nandkol-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Gangbal-Nandkol Trek'
$content = $content -replace '8 Days', '4 Days'
$content = $content -replace '13,800 ft', '12,000 ft'
$content = $content -replace 'Moderate to Challenging', 'Moderate'
$content = $content -replace 'Jul-Sep', 'Jun-Oct'
$content | Set-Content 'gangbal-nandkol-trek.html'

# Update Kousarnag Trek
$content = Get-Content 'kousarnag-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Kousarnag Lake Trek'
$content = $content -replace '8 Days', '5 Days'
$content = $content -replace '13,800 ft', '13,000 ft'
$content = $content -replace 'Moderate to Challenging', 'Moderate'
$content = $content -replace 'Jul-Sep', 'Jul-Sep'
$content | Set-Content 'kousarnag-trek.html'

# Update Sheshnag Trek
$content = Get-Content 'sheshnag-lake-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Sheshnag Lake Trek'
$content = $content -replace '8 Days', '3 Days'
$content = $content -replace '13,800 ft', '11,700 ft'
$content = $content -replace 'Moderate to Challenging', 'Easy to Moderate'
$content = $content -replace 'Jul-Sep', 'Jun-Sep'
$content | Set-Content 'sheshnag-lake-trek.html'

# Update Bandipora-Gangbal Trek
$content = Get-Content 'bandipora-gangbal-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Bandipora-Gangbal Trek'
$content = $content -replace '8 Days', '5 Days'
$content = $content -replace '13,800 ft', '11,800 ft'
$content = $content -replace 'Moderate to Challenging', 'Moderate'
$content = $content -replace 'Jul-Sep', 'Jul-Sep'
$content | Set-Content 'bandipora-gangbal-trek.html'

# Update Kolahoi Glacier Trek
$content = Get-Content 'kolahoi-glacier-trek.html' -Raw
$content = $content -replace 'Kashmir Great Lakes Trek', 'Kolahoi Glacier Trek'
$content = $content -replace '8 Days', '4 Days'
$content = $content -replace '13,800 ft', '14,100 ft'
$content = $content -replace 'Moderate to Challenging', 'Moderate to Challenging'
$content = $content -replace 'Jul-Sep', 'Jun-Sep'
$content | Set-Content 'kolahoi-glacier-trek.html'

Write-Host "All trek pages updated successfully!"
