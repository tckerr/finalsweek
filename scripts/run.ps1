Invoke-Expression ./start_mongo.ps1

write-host "Activating virtualenv..." -ForegroundColor Cyan
../.venv/Scripts/activate.ps1

write-host "Starting django server..." -ForegroundColor Cyan
python ..\finalsweek\manage.py runserver
deactivate