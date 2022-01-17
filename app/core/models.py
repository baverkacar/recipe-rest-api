from django.db import models

# Create your models here.
# Bunları araştır
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

class UserManager(BaseUserManager):

    # extra_fields demek extra bir şey eklenirse onu bu parametreye ekle demek.
    # böylece fonksiyon daha flexible oluyor
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email: 
            raise ValueError('Users must have an email adress') # email yoksa value error hatası yolladık test_models.py dosyasına
        user = self.model(email=self.normalize_email(email), **extra_fields) # case sensitive olayını çözüyoruz 
        user.set_password(password)
        user.save(using=self._db) # self._db demek değişik databesleri için olanak sağlıyor

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custem user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'    