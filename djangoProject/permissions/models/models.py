from django.db import models


class Permission(models.Model):
    permission = models.CharField(max_length=255)


class Role(models.Model):
    role = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission, related_name="role_permissions")


class User(models.Model):
    name = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role, related_name="user_roles")

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
