from django.contrib import admin
from .models import UploadedVideo,User

# Register your models here.
admin.site.register(UploadedVideo)
admin.site.register(User)
