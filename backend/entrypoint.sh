#!/bin/sh

set -e

echo "Django DB migrations..."
python manage.py migrate

echo "Coupons"

if [ "$(python manage.py coupons_count)" -eq 0 ]; then
  echo "DB is empty. Populating with some data..."
  python manage.py seed_data
else
  echo "DB is not empty. Passing..."
fi

exec "$@"