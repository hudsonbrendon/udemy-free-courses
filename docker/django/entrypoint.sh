#!/bin/bash
set -e
cmd="$@"

# This entrypoint is used to play nicely with the current cookiecutter configuration.
# Since docker-compose relies heavily on environment variables itself for configuration, we'd have to define multiple
# environment variables just to support cookiecutter out of the box. That makes no sense, so this little entrypoint
# does all this for us.
export REDIS_URL=redis://redis:6379

function mongo_ready(){
python << END
import sys
from mongoengine import connect
try:
    conn = connect()
except Exception:
    sys.exit(-1)
sys.exit(0)
END
}

until mongo_ready; do
  >&2 echo "MongoDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MongoDB is up - continuing..."
exec $cmd
