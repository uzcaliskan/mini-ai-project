import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .. import depo


def _hata(kod: int, mesaj: str) -> JsonResponse:
    return JsonResponse({"hata": mesaj}, status=kod, json_dumps_params={"ensure_ascii": False})


def ana_sayfa(istek):
    return render(istek, "sayfa.html")


@require_http_methods(["GET", "POST"])
def notlar(istek):
    yol = settings.NOTLAR_YOLU
    if istek.method == "GET":
        return JsonResponse(depo.yukle(yol), safe=False, json_dumps_params={"ensure_ascii": False})
    try:
        metin = json.loads(istek.body)["metin"].strip()
    except (ValueError, KeyError, TypeError, AttributeError):
        return _hata(400, "Geçersiz istek")
    if not metin:
        return _hata(400, "Metin boş olamaz")
    return JsonResponse(depo.ekle(yol, metin), status=201, json_dumps_params={"ensure_ascii": False})


@require_http_methods(["DELETE"])
def not_sil(istek, not_id: int):
    if depo.sil(settings.NOTLAR_YOLU, not_id):
        return JsonResponse({"silindi": True})
    return _hata(404, "Bulunamadı")
