"""
WSGI config for jnc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# ### 新的
# from pathlib import Path
import sys
# path_home = str(Path(__file__).parents[1])
# if path_home not in sys.path:
#     sys.path.append(path_home)


# # 【取代 WSGIPythonHome 、WSGIPythonPath】
# # https://stackoverflow.com/questions/75141768/how-to-deploy-multiple-django-apps-on-apache-in-windows
# # add individual virt.environment packages at the end of sys.path;  global env packages have prio
# sys.path.append('C:/xampp/htdocs/Code/project/jnc/venv')
# # replacement   WSGIPythonPath "d:/..../django_project/app_name"    
# sys.path.append('C:/xampp/htdocs/Code/project/jnc/jnc')      

# ###

"""【新找到的方法 -> 處理多個site】"""
# https://ppfocus.com/0/au2a5a8d5.html
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)  # 項目加入導包路徑
virtualenv_dir = os.path.join(PROJECT_DIR, 'venv', 'Lib', 'site-packages')  # 虛擬環境python包文件夾
sys.path.insert(0, virtualenv_dir)  # 加入導包路徑

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jnc.settings')

application = get_wsgi_application()