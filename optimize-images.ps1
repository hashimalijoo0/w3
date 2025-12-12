# Image Optimization Script
# This script compresses images using PowerShell's built-in .NET libraries

param(
    [string]$SourcePath = "c:\Users\hashi\w3\assets",
    [string]$BackupPath = "c:\Users\hashi\w3\assets_backup",
    [int]$Quality = 75
)

# Create backup directory
if (-not (Test-Path $BackupPath)) {
    New-Item -ItemType Directory -Path $BackupPath -Force | Out-Null
    Write-Host "Created backup directory: $BackupPath" -ForegroundColor Green
}

# Load required assemblies
Add-Type -AssemblyName System.Drawing

function Optimize-Image {
    param(
        [string]$ImagePath,
        [int]$Quality = 75
    )
    
    try {
        $file = Get-Item $ImagePath
        $originalSize = $file.Length / 1MB
        
        # Skip if already small
        if ($originalSize -lt 0.5) {
            Write-Host "Skipping $($file.Name) - already optimized ($([math]::Round($originalSize, 2)) MB)" -ForegroundColor Yellow
            return
        }
        
        # Create backup
        $backupFile = Join-Path $BackupPath $file.Name
        if (-not (Test-Path $backupFile)) {
            Copy-Item $ImagePath $backupFile -Force
        }
        
        # Load image
        $img = [System.Drawing.Image]::FromFile($ImagePath)
        
        # Calculate new dimensions (max 1920px width for large images)
        $maxWidth = 1920
        $newWidth = $img.Width
        $newHeight = $img.Height
        
        if ($img.Width -gt $maxWidth) {
            $ratio = $maxWidth / $img.Width
            $newWidth = $maxWidth
            $newHeight = [int]($img.Height * $ratio)
        }
        
        # Create new bitmap
        $newImg = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        $graphics = [System.Drawing.Graphics]::FromImage($newImg)
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)
        
        # Set up encoder parameters for quality
        $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $Quality)
        
        # Dispose original image before saving
        $img.Dispose()
        
        # Save optimized image
        $newImg.Save($ImagePath, $encoder, $encoderParams)
        
        # Cleanup
        $graphics.Dispose()
        $newImg.Dispose()
        
        $newSize = (Get-Item $ImagePath).Length / 1MB
        $savings = (($originalSize - $newSize) / $originalSize) * 100
        
        Write-Host "Optimized: $($file.Name)" -ForegroundColor Green
        Write-Host "  Before: $([math]::Round($originalSize, 2)) MB" -ForegroundColor Cyan
        Write-Host "  After:  $([math]::Round($newSize, 2)) MB" -ForegroundColor Cyan
        Write-Host "  Saved:  $([math]::Round($savings, 1))%" -ForegroundColor Green
        
    } catch {
        Write-Host "Error processing $ImagePath : $_" -ForegroundColor Red
    }
}

# Get all images
$images = Get-ChildItem -Path $SourcePath -Recurse -Include *.jpg,*.jpeg,*.png -File

Write-Host "`nFound $($images.Count) images to process`n" -ForegroundColor Yellow

$totalBefore = 0
$totalAfter = 0

foreach ($image in $images) {
    $sizeBefore = $image.Length
    Optimize-Image -ImagePath $image.FullName -Quality $Quality
    $sizeAfter = (Get-Item $image.FullName).Length
    
    $totalBefore += $sizeBefore
    $totalAfter += $sizeAfter
}

$totalSavings = (($totalBefore - $totalAfter) / $totalBefore) * 100

Write-Host "`n========================================" -ForegroundColor Yellow
Write-Host "OPTIMIZATION COMPLETE" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "Total size before: $([math]::Round($totalBefore / 1MB, 2)) MB" -ForegroundColor Cyan
Write-Host "Total size after:  $([math]::Round($totalAfter / 1MB, 2)) MB" -ForegroundColor Cyan
Write-Host "Total savings:     $([math]::Round($totalSavings, 1))%" -ForegroundColor Green
Write-Host "Backup location:   $BackupPath" -ForegroundColor Yellow
