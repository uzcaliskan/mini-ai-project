# 0001 – Notlar JSON dosyasında saklanır

- **Tarih:** 2026-11-02
- **Durum:** Kabul edildi

## Bağlam
Tek kullanıcılı, küçük veri; kurulum gerektirmeyen çözüm isteniyor.

## Karar
`notlar.json` dosyası kullanılır. Veritabanı (SQLite vb.) kullanılmaz.

## Sonuçlar
+ Sıfır bağımlılık, elle okunabilir.
− Büyük veride yavaşlar; eşzamanlı yazma güvenli değil.
→ Bu sınırlar sorun olursa yeni bir ADR ile kararı değiştir.
