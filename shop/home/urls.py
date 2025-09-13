from django.urls import path
from .views import (
    page_web_api_home,
    page_web_api_up,
    page_web_api_down,
    page_web_api_serach,
    tedad_page,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/home/", page_web_api_home),
    path("api/up/", page_web_api_up),
    path("api/down/", page_web_api_down),
    path("api/search/", page_web_api_serach),
    path("api/tedad/", tedad_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
