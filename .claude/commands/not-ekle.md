---
description: Uygulamaya hızlıca bir not ekler ve listeyi gösterir
argument-hint: <not metni>
allowed-tools: Bash(.venv/Scripts/python.exe:*)
---

Şu notu ekle: $ARGUMENTS

Çalıştır:
`PYTHONPATH=src .venv/Scripts/python.exe -m notlar.cli ekle "$ARGUMENTS"`
Sonra `listele` komutuyla tüm notları göster. Başka bir şey yapma.
