from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.BinaryField(max_length=60)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.username} {self.email} {self.created_at}'


class QrCode(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
