from .base import *
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-ah#jrc$=cc#j_2y@gcd1ti+*_x-ox!s%cm9l7+i7l868xpw881"
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
