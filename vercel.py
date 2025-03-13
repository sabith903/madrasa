# vercel.py
import os
from django.core.wsgi import get_wsgi_application

# Configure the environment for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'madrasa.settings')

# Get the WSGI application
application = get_wsgi_application()
app = application