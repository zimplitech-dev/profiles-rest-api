from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(
            password
        )  # set_password is the function to protect password (Encrypted to hash)
        user.save(using=self._db)  # Standard proceduce for Django to save in db

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True  # This one is not specify in UserProfile class --> But automatically specify by PermissionsMixin
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """Database model for users in the system"""

#     email = models.EmailField(
#         max_length=255, unique=True
#     )  # This one is to create email
#     name = models.CharField(
#         max_length=255
#     )  # This one is to create name (No need to be unique)
#     is_active = models.BooleanField(
#         default=True
#     )  # This is to check whether user us active
#     is_staff = models.BooleanField(default=False)  # by default --> False

#     objects = UserProfileManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name"]

#     def get_full_name(self):
#         """Retrieve full name of user"""
#         return self.name

#     def get_short_name(self):
#         """Retrieve short name of user"""
#         return self.name

#     def __str__(self):
#         """Return string representation of our user"""
#         return self.email
