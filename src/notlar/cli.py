"""Komut satırı: python -m notlar.cli ekle|listele|sil"""
import argparse
from pathlib import Path

from . import depo

VARSAYILAN = Path("notlar.json")


def main(argv=None, yol: Path = VARSAYILAN) -> int:
    p = argparse.ArgumentParser(prog="notlar")
    alt = p.add_subparsers(dest="komut", required=True)
    alt.add_parser("listele")
    e = alt.add_parser("ekle")
    e.add_argument("metin")
    s = alt.add_parser("sil")
    s.add_argument("id", type=int)
    a = p.parse_args(argv)

    if a.komut == "ekle":
        n = depo.ekle(yol, a.metin)
        print(f"Eklendi #{n['id']}")
    elif a.komut == "listele":
        for n in depo.yukle(yol):
            print(f"#{n['id']} {n['metin']}")
    elif a.komut == "sil":
        print("Silindi" if depo.sil(yol, a.id) else "Bulunamadı")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
