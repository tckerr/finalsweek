param(
    [switch]$s = $false
)

write-host "Installing VirtualEnv..." -ForegroundColor Cyan
pip install virtualenv

write-host "Creating local .venv directory..." -ForegroundColor Cyan
$TARGETDIR = '.venv'
if(!(Test-Path -Path $TARGETDIR )){
	virtualenv .venv
} else {
	write-host "Skipping, already exists"
}

write-host "Activating virtual environment..." -ForegroundColor Cyan
./.venv/Scripts/activate.ps1

write-host "Installing project dependencies..." -ForegroundColor Cyan
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter

write-host "Running initial migration..." -ForegroundColor Cyan
./finalsweek/migrate.ps1


if($s){
    write-host "Creating superuser..." -ForegroundColor Cyan
    python finalsweek/manage.py createsuperuser
}

deactivate
write-host "Done!" -ForegroundColor Green