"""Notları JSON dosyasında saklayan basit depo (bkz. docs/kararlar/0001)."""
import json
from pathlib import Path


def yukle(yol: Path) -> list[dict]:
    if not yol.exists():
        return []
    return json.loads(yol.read_text(encoding="utf-8"))


def kaydet(yol: Path, notlar: list[dict]) -> None:
    yol.write_text(json.dumps(notlar, ensure_ascii=False, indent=2), encoding="utf-8")


def ekle(yol: Path, metin: str) -> dict:
    notlar = yukle(yol)
    yeni = {"id": max((n["id"] for n in notlar), default=0) + 1, "metin": metin}
    notlar.append(yeni)
    kaydet(yol, notlar)
    return yeni


def sil(yol: Path, not_id: int) -> bool:
    notlar = yukle(yol)
    kalan = [n for n in notlar if n["id"] != not_id]
    kaydet(yol, kalan)
    return len(kalan) != len(notlar)
