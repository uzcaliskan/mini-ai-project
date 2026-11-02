# Notlar – Claude Code öğrenme projesi

Küçük bir not defteri CLI'ı. Asıl amaç uygulama değil, Claude Code kavramlarını (CLAUDE.md, skill, komut, subagent, hook, eklenti) minyatür ölçekte görmek.

## Komutlar
- Python 3.13.14 (uv ile indirilen yönetilen Python; sistemdeki `Programs\Python` klasörü bozuk, kullanma)
- Sanal ortam: `.venv` (paketleri HER ZAMAN buraya kur: `.venv\Scripts\python -m pip install ...`)
- Test: `.venv\Scripts\python -m pytest`
- Çalıştır: `.venv\Scripts\python -m notlar.cli ekle "metin"` (`PYTHONPATH=src` gerekir)

- Web arayüzü (Django, karar 0005): `.venv\Scripts\python manage.py runserver` → http://127.0.0.1:8000 (`PYTHONPATH` gerekmez). Alternatif: `PYTHONPATH=src` ile `-m notlar.web`.

## MCP
- `context7` (`.mcp.json`): güncel kütüphane dökümantasyonu. Kütüphane/API sorularında prompt'a "use context7" ekle.

## Kurallar
- Kod ve yorumlar Türkçe, isimler Türkçe.
- Depolama JSON'dur; veritabanı ekleme (bkz. docs/kararlar/0001).
- Her davranış değişikliğine test yaz.

## Proje hafızası (okuma sırası)
1. `docs/baglam/baglam.md` – proje neden var, hedefler, kapsam (aynı klasörde fotoğraf vb. ekler)
2. `docs/kararlar/` – alınmış kararlar (ADR). Çelişen bir şey yapmadan önce oku.
3. `docs/oturum-gunlugu.md` – son oturumlarda ne yapıldı

Bu hafızayı güncellemek için `proje-hafizasi` skill'ini kullan (`/proje-hafizasi`).
