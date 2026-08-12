#!/bin/sh

set -e

if [ "$RUN_MIGRATIONS" = "true" ]; then
    echo "Running migrations..."
    uv run alembic upgrade head
fi

exec "$@"