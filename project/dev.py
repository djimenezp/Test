from .settings import *

assert BASE_DIR
SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-upnfygsoga2)v6ngphwzelinh58w&id$w&bik(k=)=yyb(@$mc')

DEBUG = int(os.environ.get("DEBUG", default=1))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "*").split(" ")
