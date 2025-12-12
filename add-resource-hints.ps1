# Script to add performance optimizations to all HTML files
param(
    [string]$Directory = "c:\Users\hashi\w3"
)

$resourceHints = @"
    <!-- Performance Optimizations -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    <link rel="dns-prefetch" href="https://images.pexels.com">
"@

# Get all HTML files
$htmlFiles = Get-ChildItem -Path $Directory -Filter "*.html" -File

Write-Host "Found $($htmlFiles.Count) HTML files to optimize`n" -ForegroundColor Yellow

foreach ($file in $htmlFiles) {
    try {
        $content = Get-Content $file.FullName -Raw
        
        # Check if already optimized
        if ($content -match "Performance Optimizations") {
            Write-Host "Skipping $($file.Name) - already optimized" -ForegroundColor Yellow
            continue
        }
        
        # Add resource hints after <head> tag
        if ($content -match "(<head>)") {
            $content = $content -replace "(<head>)", "`$1`r`n$resourceHints"
            
            # Update font loading to use display=swap
            $content = $content -replace "family=Inter:wght@300;400;700;800&display=swap", "family=Inter:wght@300;400;700;800&display=swap"
            $content = $content -replace "family=Inter:wght@300;400;700&display=swap", "family=Inter:wght@300;400;700;800&display=swap"
            
            # Save the file
            Set-Content -Path $file.FullName -Value $content -NoNewline
            
            Write-Host "Optimized: $($file.Name)" -ForegroundColor Green
        }
        else {
            Write-Host "Skipped $($file.Name) - no <head> tag found" -ForegroundColor Red
        }
        
    }
    catch {
        Write-Host "Error processing $($file.Name): $_" -ForegroundColor Red
    }
}

Write-Host "`nOptimization complete!" -ForegroundColor Green
