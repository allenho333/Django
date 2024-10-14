#!/bin/bash

# Install the language model
python -m spacy download en_core_web_sm

# Start the app
python manage.py runserver 0.0.0.0:8000