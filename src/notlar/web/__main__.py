import os
import sys

from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notlar.web.ayarlar")
# Otomatik yeniden yükleyici kapalı: tek süreç, yerel kullanım.
execute_from_command_line([sys.argv[0], "runserver", "--noreload", "127.0.0.1:8000"])
