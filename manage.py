#!/usr/bin/env python
"""Django komut satırı aracı (bkz. docs/kararlar/0005).

Örnek: python manage.py runserver
"""
import os
import sys
from pathlib import Path

# src/ klasörünü yola ekler; PYTHONPATH=src ayarlamaya gerek kalmaz.
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notlar.web.ayarlar")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
