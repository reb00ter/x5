#!/bin/bash

cd js
npm install
npm run build
cd ..
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

