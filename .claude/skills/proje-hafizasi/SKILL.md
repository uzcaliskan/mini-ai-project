---
name: proje-hafizasi
description: Proje hafızasını okur ve günceller (bağlam, kararlar/ADR, oturum günlüğü). Kullanıcı "karar al/kaydet", "hafızayı güncelle", "bu projede ne yapmıştık", "oturumu kapat" dediğinde veya mimari bir tercih yapıldığında kullan.
---

# Proje Hafızası

Hafıza `docs/` altında düz Markdown dosyalarıdır. Üç katman vardır:

| Katman | Dosya | Ne zaman değişir |
|---|---|---|
| Bağlam | `docs/baglam/baglam.md` | Proje amacı/kapsamı değişince |
| Kararlar | `docs/kararlar/NNNN-baslik.md` | Önemli bir teknik tercih yapılınca |
| Günlük | `docs/oturum-gunlugu.md` | Her oturum sonunda |

## Mod 1 – Hatırla (okuma)
1. `docs/baglam/baglam.md`, `docs/kararlar/` içindeki tüm dosyalar ve günlüğün ilk ~30 satırını oku.
2. Kullanıcıya 5 maddeyi geçmeyen özet ver: amaç, geçerli kararlar, son yapılanlar, sıradaki adım.

## Mod 2 – Karar kaydet
1. `docs/kararlar/` içindeki en büyük numarayı bul, +1 ver (4 haneli).
2. `docs/kararlar/_sablon.md` şablonunu kopyala: Bağlam / Karar / Sonuçlar.
3. Mevcut bir kararı **silme**; değişiyorsa eskisinin durumunu `Yerine geçildi: NNNN` yap ve yeni ADR yaz.
4. Günlüğe tek satır ekle.

## Mod 3 – Oturumu kapat
1. `docs/oturum-gunlugu.md` en üstüne bugünün tarihiyle kısa madde listesi ekle (yapılan, açık kalan, sıradaki).
2. Yeni karar alındıysa Mod 2'yi çalıştır.

## Kurallar
- Kısa yaz; her kayıt birkaç satır olsun.
- Kod okunarak anlaşılabilen şeyleri hafızaya yazma; sadece **neden**'i yaz.
