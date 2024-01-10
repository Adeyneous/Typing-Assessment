import os

app.config.from_pyfile('config.py')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'default_key_if_not_set')
