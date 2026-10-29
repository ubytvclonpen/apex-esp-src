param(
    [string]$DriverPath = "build\\apex_esp_km.sys",
    [string]$CertSubject = "apex-esp-src-dev"
)

Write-Host "Signing $DriverPath with $CertSubject"
signtool sign /fd SHA256 /n $CertSubject $DriverPath
if ($LASTEXITCODE -ne 0) { throw "signtool failed" }