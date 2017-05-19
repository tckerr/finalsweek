#!/usr/bin/env bash

REPODIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../.. && pwd )"
source $REPODIR/.venv/bin/activate
python $REPODIR/finalsweek/manage.py create_single