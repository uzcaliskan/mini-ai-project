import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from notlar import depo


def test_ekle_ve_yukle(tmp_path):
    yol = tmp_path / "n.json"
    depo.ekle(yol, "süt al")
    depo.ekle(yol, "kod yaz")
    assert [n["id"] for n in depo.yukle(yol)] == [1, 2]


def test_sil(tmp_path):
    yol = tmp_path / "n.json"
    depo.ekle(yol, "a")
    assert depo.sil(yol, 1) is True
    assert depo.sil(yol, 1) is False
