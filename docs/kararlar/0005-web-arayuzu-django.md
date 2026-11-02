# 0005 – Web arayüzü Django ile yapılır

- **Tarih:** 2026-11-02
- **Durum:** Kabul edildi

## Bağlam
Kullanıcı web arayüzünün Django ile yapılmasını istedi. Bu, 0004'ü (`http.server`, çerçeve yok) ve 0002'nin "çalışma zamanı bağımlılığı yok" kuralını değiştiriyor.

## Karar
`src/notlar/web/` bir Django paketidir (ayarlar, urller, görünümler, şablon). Çalıştırma: `python -m notlar.web`. Depolama değişmez: `depo.py` + JSON, Django ORM/veritabanı kullanılmaz (`DATABASES = {}`, bkz. 0001). CSRF koruması açık; sayfadaki JS token'ı `X-CSRFToken` başlığıyla gönderir. Bağımlılık `requirements.txt`'te sabit aralıkla tutulur (`django>=5.2,<6`).

## Sonuçlar
+ Yönlendirme, şablon ve CSRF hazır; Django'yu öğrenmek için gerçek bir örnek.
− Çalışma zamanı bağımlılığı oldu: CLI hâlâ yalnızca standart kütüphane kullanır, web yüzü Django ister.
− Yalnızca yerel kullanım: `DEBUG=True`, geliştirme `SECRET_KEY`'i, kimlik doğrulama yok. Uzak sunucuya açılacaksa yeni ADR gerekir.
− Eşzamanlı yazma güvenli değil (0001'deki sınır geçerli).
