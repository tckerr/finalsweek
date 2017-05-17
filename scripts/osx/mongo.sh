#!/usr/bin/env bash

REPODIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd ../.. && pwd )"
mongod --dbpath $REPODIR/data/mongo --port=8001