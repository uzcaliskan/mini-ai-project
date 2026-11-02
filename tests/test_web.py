import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notlar.web.ayarlar")

import django
import pytest
from django.test import Client
from django.test.utils import override_settings

django.setup()


@pytest.fixture
def istemci(tmp_path):
    with override_settings(NOTLAR_YOLU=tmp_path / "n.json"):
        yield Client(enforce_csrf_checks=True)


def _csrf(istemci):
    istemci.get("/")
    return {"HTTP_X_CSRFTOKEN": istemci.cookies["csrftoken"].value}


def _post(istemci, veri):
    return istemci.post("/api/notlar", json.dumps(veri), content_type="application/json", **_csrf(istemci))


def test_ana_sayfa_html_doner(istemci):
    yanit = istemci.get("/")
    assert yanit.status_code == 200 and b"<h1>Notlar</h1>" in yanit.content


def test_ekle_listele_sil(istemci):
    yanit = _post(istemci, {"metin": "süt al"})
    assert yanit.status_code == 201 and yanit.json()["id"] == 1
    assert [n["metin"] for n in istemci.get("/api/notlar").json()] == ["süt al"]
    assert istemci.delete("/api/notlar/1", **_csrf(istemci)).status_code == 200
    assert istemci.delete("/api/notlar/1", **_csrf(istemci)).status_code == 404


def test_bos_metin_reddedilir(istemci):
    assert _post(istemci, {"metin": "   "}).status_code == 400
    assert _post(istemci, {"yanlis": 1}).status_code == 400


def test_csrf_olmadan_yazma_reddedilir(istemci):
    yanit = istemci.post("/api/notlar", json.dumps({"metin": "x"}), content_type="application/json")
    assert yanit.status_code == 403
