# 0002 – Uygulama yalnızca standart kütüphane kullanır

- **Tarih:** 2026-11-02
- **Durum:** Kabul edildi

## Karar
Çalışma zamanı bağımlılığı yok (argparse, json, pathlib). Sadece geliştirme aracı olarak `pytest` kurulur, `.venv` içine.

## Sonuçlar
Paket kurma alışkanlığını (sanal ortam önce, sonra pip) göstermek için pytest yeterli.
