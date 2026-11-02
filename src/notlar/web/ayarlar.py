"""Django ayarları. Veritabanı yok; notlar depo.py ile JSON'da tutulur (bkz. 0001)."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Yalnızca yerel kullanım (bkz. 0005): geliştirme anahtarı, DEBUG açık.
SECRET_KEY = "yerel-gelistirme-anahtari-uretimde-kullanma"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]

NOTLAR_YOLU = Path(os.environ.get("NOTLAR_YOLU", "notlar.json"))

INSTALLED_APPS = []
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]
ROOT_URLCONF = "notlar.web.urller"
DATABASES = {}
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "sablonlar"],
}]
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
USE_TZ = True
LANGUAGE_CODE = "tr"
