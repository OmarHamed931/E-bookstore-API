from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)

    email = models.EmailField(max_length=100, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    id = models.AutoField(primary_key=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username