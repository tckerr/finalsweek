#!/usr/bin/env bash

FORCE=0
SUPERUSER=0

while getopts "::sf" OPTIONS; do
    case $OPTIONS in
        f)
            FORCE=1
            ;;
        s)
            SUPERUSER=1
            ;;
        *)
            echo "UNKNOWN ARG!"
            exit 1
    esac
done

printf "Setting preferences..."
set -e

printf "\nSetting permissions.."
REPODIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../.. && pwd )"
sudo chmod 777 "$REPODIR"

deactivate || printf "Tried to deactivate, but no VirtualEnv was activated"

printf "\nInstalling VirtualEnv..."
python3 -m pip install virtualenv

printf "\nSetting up local .venv directory..."
VENVDIR="$REPODIR/.venv"
if [ -d "$VENVDIR" ]; then
    printf "\nAlready exists in $VENVDIR..."

    if (( $FORCE==1 )); then
        printf "\nForce option specified, removing $VENVDIR..."
        rm -rd $VENVDIR
        printf "\nInstalling to $VENVDIR"
        virtualenv $VENVDIR -p python3
    fi
  else
    printf "\nInstalling to $VENVDIR"
    virtualenv $VENVDIR -p python3
fi

printf "\nActivating virtual environment..."
source $VENVDIR/bin/activate

printf "\nInstalling project dependencies..."
pip install -r $REPODIR/requirements.txt

printf "\nRunning initial migration..."
python $REPODIR/finalsweek/manage.py migrate

if (( $SUPERUSER==1 )); then
    printf "\nCreating superuser..."
    python $REPODIR/finalsweek/manage.py createsuperuser
fi

printf "\nInstalling mongo..."
brew install mongodb
MONGODIR="$REPODIR/data/mongo"
mkdir -p $MONGODIR
sudo chmod 777 "$MONGODIR"

printf "\nSetting permissions..."
sudo chmod 777 "$REPODIR"

deactivate
printf "\nDone!"