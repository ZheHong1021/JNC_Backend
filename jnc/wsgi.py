"""
WSGI config for jnc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

### 新的
from pathlib import Path
import sys
path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)
###

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jnc.settings')

application = get_wsgi_application()