from rest_framework import serializers

from djangoProject.permissions.models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(source="roles", many=True)

    class Meta:
        model = User
        fields = ["name", "role"]
