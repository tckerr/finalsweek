param(
    [switch]$s = $false,
    [switch]$f = $false
)

write-host "Setting preferences..." -ForegroundColor Cyan
$ErrorActionPreference = "Stop"

write-host "Ensuring no VirtualEnv is running..." -ForegroundColor Cyan
Try { 
    deactivate 
} 
Catch {
    write-host "Tried to deactivate, but no VirtualEnv was activated" -ForegroundColor Magenta
}

write-host "Installing VirtualEnv..." -ForegroundColor Cyan
pip install virtualenv

write-host "Creating local .venv directory..." -ForegroundColor Cyan
$VENV_DIR = "$($PSScriptRoot)/../.venv"
if(!(Test-Path -Path $VENV_DIR )){
	virtualenv $VENV_DIR
} else {
	if($f){
        write-host "VirtualEnv exists. Recreating..." -ForegroundColor Magenta
        rm $VENV_DIR -Recurse
        virtualenv $VENV_DIR
    } else {
        write-host "VirtualEnv exists. Skipping..." -ForegroundColor Magenta
    }
}

write-host "Activating virtual environment..." -ForegroundColor Cyan
& "$($VENV_DIR)/Scripts/activate.ps1"

write-host "Installing project dependencies..." -ForegroundColor Cyan
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install wheel

# this one is tricky, try these first:
#     https://dev.mysql.com/downloads/file/?id=378015
#     http://stackoverflow.com/questions/2817869/error-unable-to-find-vcvarsall-bat
pip install "../lib/mysqlclient-1.3.10-cp34-cp34m-win_amd64.whl"

write-host "Running initial migration..." -ForegroundColor Cyan
./migrate.ps1

if($s){
    write-host "Creating superuser..." -ForegroundColor Cyan
    python finalsweek/manage.py createsuperuser
}

deactivate
write-host "Done!" -ForegroundColor Green