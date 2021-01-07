#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

export INIT=${INIT:='no'}

if [ "${INIT}" = "yes" ]; then
   bash scripts/init_db.sh
fi

exec "$@"
