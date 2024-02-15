from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
