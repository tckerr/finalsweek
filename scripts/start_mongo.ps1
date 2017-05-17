write-host "Stopping MongoDB service..." -ForegroundColor Cyan
net stop MongoDB

write-host "Running repairs to be safe..." -ForegroundColor Cyan
mongod --repair --dbpath $PSScriptRoot/../data/mongo > $null

write-host "Starting MongoDB service..." -ForegroundColor Cyan
net start MongoDB