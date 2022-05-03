from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User as UserBase

class AuditModel(models.Model):
    """Base Model to audit other models"""

    created_at  = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='Modificado em',
        auto_now=True
    )
