# 0004 – Web arayüzü standart kütüphane `http.server` ile yapılır

- **Tarih:** 2026-11-02
- **Durum:** Yerine geçildi: 0005

## Bağlam
Playwright ve Chrome DevTools MCP'lerini denemek için tarayıcıda açılabilen bir arayüz gerekti. Proje CLI'dı, web yüzü yoktu.

## Karar
`src/notlar/web.py`, `http.server` ile tek sayfa HTML + küçük JSON API (`/api/notlar`) sunar. Flask/FastAPI gibi çerçeve eklenmez (bkz. 0002). Depolama aynı kalır: `depo.py` + JSON (bkz. 0001).

## Sonuçlar
+ Sıfır bağımlılık; CLI ile aynı `depo.py` paylaşılır.
− Üretim sunucusu değil; yalnızca yerel (127.0.0.1) kullanım, kimlik doğrulama yok.
− Eşzamanlı yazma güvenli değil (0001'deki sınır web için de geçerli).
