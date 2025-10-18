#!/usr/bin/env sh
set -e

# Wait for MySQL to be ready
if [ -n "$DB_HOST" ]; then
  echo "Waiting for DB $DB_HOST:$DB_PORT..."
  until nc -z "$DB_HOST" "$DB_PORT"; do
    sleep 1
  done
fi

exec "$@"


