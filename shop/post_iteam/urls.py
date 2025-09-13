from django.urls import path
from .views import post_page_web_iteam
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , post_page_web_iteam),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
