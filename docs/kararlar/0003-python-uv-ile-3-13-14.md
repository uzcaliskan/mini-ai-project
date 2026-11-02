# 0003 – Python 3.13.14, uv ile indirilen yönetilen sürümden kullanılır

- **Tarih:** 2026-11-02
- **Durum:** Kabul edildi

## Bağlam
Sistemdeki `AppData\Local\Programs\Python` klasöründe, kurulumların üstünde `pyvenv.cfg` dosyaları var. Bu yüzden oradan açılan her ortam 3.12.2'ye bağlanıyor. Resmi yükleyiciyle global kurulum da `0x80070641` hatasıyla başarısız oldu.

## Karar
`.venv`, `uv venv --python 3.13.14 --managed-python` ile kurulur. Python `AppData\Roaming\uv\python` altına indirilir. Sistemdeki bozuk kurulumlar kullanılmaz.

## Sonuçlar
+ Sistem Python'una dokunmadan, tekrarlanabilir kurulum.
− `.venv` uv'nin indirdiği klasöre bağlı; o klasör silinirse ortam bozulur.
→ Yeniden kurmak için `uv`'u indirip aynı komutu çalıştır, sonra `pip install -r requirements.txt`.
