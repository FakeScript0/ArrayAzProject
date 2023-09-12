from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profile_photo/", blank=True, null=True,)
    # ...

    def __str__(self):
        return self.user.username
# Create your models here.
