# Oturum günlüğü

Yeni kayıtlar en üste eklenir.

## 2026-11-02 (dördüncü oturum, devam)
- Web sayfası çizgili not defteri görünümüne çevrildi.
- Kullanıcı isteğiyle web arayüzü Django'ya taşındı (karar 0005; 0004 yerine geçildi, 0002 web için kısmen). `web.py` silindi, `src/notlar/web/` paketi eklendi, testler Django istemcisine çevrildi (CSRF dahil), `requirements.txt`'e django eklendi.
- `manage.py` eklendi: `python manage.py runserver` (PYTHONPATH gerekmez). Chrome DevTools ile ekleme/silme elle denendi, çalışıyor.
- Açık: GITHUB_PAT/github MCP hâlâ bağlanmıyor; sistemdeki bozuk `Programs\Python` temizlenmedi.

## 2026-11-02 (dördüncü oturum)
- `baglam.md` kapsamı web arayüzünü içerecek şekilde düzeltildi (karar 0004 ile çelişiyordu).
- Fotoğraf vb. ekler için `docs/baglam/` klasörü açıldı; `baglam.md` buraya taşındı (CLAUDE.md ve iki SKILL.md yolu güncellendi).
- Açık: github MCP bağlanmadı (`GITHUB_PAT`).

## 2026-11-02 (üçüncü oturum)
- `.mcp.json`'a playwright, chrome-devtools ve github (http, `${GITHUB_PAT}`) MCP sunucuları eklendi; henüz bağlantı denenmedi.
- MCP'leri denemek için `web.py` (web arayüzü) + `tests/test_web.py` yazıldı, testler geçiyor (karar 0004).
- Miro MCP (http, OAuth) `.mcp.json`'a eklendi.
- `git init -b main` yapıldı; ilk commit GitHub'a (`uzcaliskan/mini-ai-project`) gönderildi.
- Açık: `GITHUB_PAT` tanımlı değil, `gh` kurulu değil. `.claude/settings.local.json` .gitignore'a eklendi.
- Sıradaki: Claude Code'u yeniden başlat, `/mcp` ile kontrol et, Playwright/DevTools ile `localhost:8000`'i dene.

## 2026-11-02 (ikinci oturum)
- `.venv` 3.12.2'ye bağlanıyordu; neden sistemdeki `pyvenv.cfg` dosyalarıydı. 3.13.14 uv ile kuruldu (karar 0003).
- `Python313\pyvenv.cfg` geçici olarak yeniden adlandırılmıştı, eski haline alındı. `Programs\Python\pyvenv.cfg` dokunulmadı.
- Açık: sistemdeki bozuk `Programs\Python` klasörü temizlenmedi.
- Sıradaki: `/not-ekle`, `kod-gozden-gecirici` ve hook'u dene.

## 2026-11-02
- Proje iskeleti, `.venv`, pytest kuruldu.
- depo.py + cli.py yazıldı, testler eklendi.
- Hafıza yapısı (CLAUDE.md, baglam, kararlar), skill, komut, subagent, hook ve eklenti örneği oluşturuldu.
- Sıradaki: `/not-ekle` komutunu dene, `proje-hafizasi` skill'ini bir karar eklemek için çalıştır.
