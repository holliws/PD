$apturetie = Get-Service |
    Where-Object { $_.Status -eq "Stopped" } |
    Sort-Object Name |
    Select-Object Name, Status |
$apturetie |Export-Csv -Path "apturetie.csv" -Delimiter ","
Write-Host"fails gatavs"

