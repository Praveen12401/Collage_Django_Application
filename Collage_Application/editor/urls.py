from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='edit_video'),
    path("contact_us/",views.contact_view,name='contact_us'),
    path("user_form/",views.user_form,name='user_form'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
