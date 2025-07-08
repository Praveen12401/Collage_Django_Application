from django.urls import path
from . import views

urlpatterns = [
    path('', views.edit_video, name='edit_video'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
