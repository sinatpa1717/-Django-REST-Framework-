from django.urls import path
from .views import MY_ss

urlpatterns = [
    path("api/auth/", MY_ss.as_view()),
]
