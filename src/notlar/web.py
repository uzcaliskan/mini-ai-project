"""Notlar için küçük web arayüzü (yalnızca standart kütüphane, bkz. docs/kararlar/0002).

Çalıştır: python -m notlar.web  ->  http://127.0.0.1:8000
"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import depo

VARSAYILAN = Path("notlar.json")

SAYFA = """<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Notlar</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 32rem; margin: 2rem auto; padding: 0 1rem; }
    form { display: flex; gap: .5rem; }
    input { flex: 1; padding: .5rem; }
    ul { list-style: none; padding: 0; }
    li { display: flex; justify-content: space-between; padding: .5rem 0; border-bottom: 1px solid #ddd; }
    #bos { color: #777; }
  </style>
</head>
<body>
  <h1>Notlar</h1>
  <form id="form">
    <input id="metin" placeholder="Yeni not" aria-label="Yeni not" required>
    <button type="submit">Ekle</button>
  </form>
  <p id="bos" hidden>Henüz not yok.</p>
  <ul id="liste"></ul>
  <script>
    const liste = document.getElementById("liste");
    const bos = document.getElementById("bos");

    async function yenile() {
      const notlar = await (await fetch("/api/notlar")).json();
      bos.hidden = notlar.length > 0;
      liste.replaceChildren(...notlar.map(n => {
        const li = document.createElement("li");
        const span = document.createElement("span");
        span.textContent = n.metin;
        const btn = document.createElement("button");
        btn.textContent = "Sil";
        btn.onclick = async () => { await fetch("/api/notlar/" + n.id, { method: "DELETE" }); yenile(); };
        li.append(span, btn);
        return li;
      }));
    }

    document.getElementById("form").onsubmit = async e => {
      e.preventDefault();
      const girdi = document.getElementById("metin");
      await fetch("/api/notlar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ metin: girdi.value }),
      });
      girdi.value = "";
      yenile();
    };

    yenile();
  </script>
</body>
</html>
"""


def isleyici_olustur(yol: Path):
    class Isleyici(BaseHTTPRequestHandler):
        def _gonder(self, kod: int, govde: bytes, tur: str = "application/json; charset=utf-8"):
            self.send_response(kod)
            self.send_header("Content-Type", tur)
            self.send_header("Content-Length", str(len(govde)))
            self.end_headers()
            self.wfile.write(govde)

        def _json(self, kod: int, veri):
            self._gonder(kod, json.dumps(veri, ensure_ascii=False).encode("utf-8"))

        def do_GET(self):
            if self.path == "/":
                self._gonder(200, SAYFA.encode("utf-8"), "text/html; charset=utf-8")
            elif self.path == "/api/notlar":
                self._json(200, depo.yukle(yol))
            else:
                self._json(404, {"hata": "Bulunamadı"})

        def do_POST(self):
            if self.path != "/api/notlar":
                return self._json(404, {"hata": "Bulunamadı"})
            try:
                uzunluk = int(self.headers.get("Content-Length", 0))
                metin = json.loads(self.rfile.read(uzunluk))["metin"].strip()
            except (ValueError, KeyError, TypeError, AttributeError):
                return self._json(400, {"hata": "Geçersiz istek"})
            if not metin:
                return self._json(400, {"hata": "Metin boş olamaz"})
            self._json(201, depo.ekle(yol, metin))

        def do_DELETE(self):
            onek = "/api/notlar/"
            if not self.path.startswith(onek) or not self.path[len(onek):].isdigit():
                return self._json(404, {"hata": "Bulunamadı"})
            if depo.sil(yol, int(self.path[len(onek):])):
                self._json(200, {"silindi": True})
            else:
                self._json(404, {"hata": "Bulunamadı"})

        def log_message(self, *args):
            pass

    return Isleyici


def sunucu_olustur(yol: Path = VARSAYILAN, port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port), isleyici_olustur(yol))


if __name__ == "__main__":
    s = sunucu_olustur()
    print(f"http://127.0.0.1:{s.server_address[1]}")
    s.serve_forever()
