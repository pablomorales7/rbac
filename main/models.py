# core/models.py

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('teacher', 'Docente'),
        ('student', 'Estudiante'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='admin'
    )

    phone = models.CharField(
        max_length=20
    )

    signup_time = models.DateTimeField(
        default=timezone.now
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class AuditLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=200
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    def __str__(self):
        usuario = self.user.username if self.user else "Desconocido"
        return f"{usuario} - {self.action} - {self.timestamp}"