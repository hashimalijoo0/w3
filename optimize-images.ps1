# PowerShell script to optimize images in standard web formats
# Requires .NET System.Drawing

Add-Type -AssemblyName System.Drawing

$assetsPath = "$PSScriptRoot\assets"
$quality = 85

function Optimize-Image {
    param (
        [string]$filePath
    )

    try {
        $image = [System.Drawing.Image]::FromFile($filePath)
        
        # Check if resize is needed (max width 1920)
        $newWidth = $image.Width
        $newHeight = $image.Height
        $wasResized = $false

        if ($image.Width -gt 1920) {
            $ratio = 1920 / $image.Width
            $newWidth = 1920
            $newHeight = [int]($image.Height * $ratio)
            $wasResized = $true
        }

        # Create new bitmap
        $bmp = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
        $graph = [System.Drawing.Graphics]::FromImage($bmp)
        $graph.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graph.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graph.DrawImage($image, 0, 0, $newWidth, $newHeight)

        # Copmpression Encoder
        $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
        $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
        $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, $quality)

        $image.Dispose() # Release original file

        # Save back to file
        $bmp.Save($filePath, $codec, $encoderParams)
        $bmp.Dispose()
        $graph.Dispose()

        Write-Host "Optimized: $filePath"
    }
    catch {
        Write-Host "Failed to optimize: $filePath - $_"
    }
}

# Find all JPG/JPEG/PNG images
Get-ChildItem -Path $assetsPath -Recurse -Include *.jpg, *.jpeg, *.png | ForEach-Object {
    $sizeKB = $_.Length / 1KB
    if ($sizeKB -gt 500) {
        Write-Host "Optimizing large file: $($_.Name) ($([math]::round($sizeKB)) KB)"
        Optimize-Image -filePath $_.FullName
    }
}
