import json
import sys
import threading
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pytest

from notlar import web


@pytest.fixture
def adres(tmp_path):
    sunucu = web.sunucu_olustur(tmp_path / "n.json", port=0)
    threading.Thread(target=sunucu.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{sunucu.server_address[1]}"
    sunucu.shutdown()
    sunucu.server_close()


def istek(adres, yol, yontem="GET", veri=None):
    govde = json.dumps(veri).encode() if veri is not None else None
    r = urllib.request.Request(adres + yol, data=govde, method=yontem,
                               headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r) as yanit:
            return yanit.status, yanit.read()
    except urllib.error.HTTPError as h:
        return h.code, h.read()


def test_ana_sayfa_html_doner(adres):
    kod, govde = istek(adres, "/")
    assert kod == 200 and b"<h1>Notlar</h1>" in govde


def test_ekle_listele_sil(adres):
    kod, govde = istek(adres, "/api/notlar", "POST", {"metin": "süt al"})
    assert kod == 201 and json.loads(govde)["id"] == 1
    _, govde = istek(adres, "/api/notlar")
    assert [n["metin"] for n in json.loads(govde)] == ["süt al"]
    assert istek(adres, "/api/notlar/1", "DELETE")[0] == 200
    assert istek(adres, "/api/notlar/1", "DELETE")[0] == 404


def test_bos_metin_reddedilir(adres):
    assert istek(adres, "/api/notlar", "POST", {"metin": "   "})[0] == 400
    assert istek(adres, "/api/notlar", "POST", {"yanlis": 1})[0] == 400
