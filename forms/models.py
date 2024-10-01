from django.db import models

class UserInfoModel(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='uploaded')
