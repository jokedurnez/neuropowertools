#!/bin/bash

source activate neuropower

python manage.py flush --no-input
python manage.py migrate

exec "$@"