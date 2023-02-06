from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER')
    )
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, related_name='users', on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=6, choices=ROLES, default='USER')
    created_by = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

