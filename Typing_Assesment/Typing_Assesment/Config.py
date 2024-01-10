# config.py
import os
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'default_key_if_not_set')
