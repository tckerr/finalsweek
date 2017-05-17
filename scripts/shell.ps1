../.venv/Scripts/activate.ps1
python $PSScriptRoot/../finalsweek/manage.py shell_plus
write-host "Closing virtualenv..." -ForegroundColor Cyan
deactivate