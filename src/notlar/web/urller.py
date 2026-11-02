from django.urls import path

from . import gorunumler

urlpatterns = [
    path("", gorunumler.ana_sayfa),
    path("api/notlar", gorunumler.notlar),
    path("api/notlar/<int:not_id>", gorunumler.not_sil),
]
