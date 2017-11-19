#!/bin/sh

echo "yes" | python3 manage.py setup_db
echo "yes" | python3 manage.py load_all

exec "$@"
