from rest_framework import serializers

from .models import (
    ActionType,
    ClientType,
    Country,
    Function,
    Module,
    Role,
    VirtualAgentType,
)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = "__all__"


class VirtualAgentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAgentType
        fields = "__all__"


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = "__all__"
