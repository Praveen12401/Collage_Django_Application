from django.db import models

 

class UploadedVideo(models.Model):
    name=models.CharField(max_length=100,default='first')
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name