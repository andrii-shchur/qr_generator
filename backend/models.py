from django.db import models
from django.conf import settings
from django.utils import timezone


class QrCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img_path = models.FilePathField(path='/static/img')
    created_at = models.DateTimeField(default=str(timezone.now()))

    def __str__(self):
        return f'{self.user_id} {self.img_path}'
