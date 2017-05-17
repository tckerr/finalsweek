#!/usr/bin/env bash

REPODIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../.. && pwd )"
source $REPODIR/.venv/bin/activate
python3 $REPODIR/finalsweek/manage.py runserver 8000