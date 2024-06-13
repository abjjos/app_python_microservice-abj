from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_extension = models.CharField(max_length=10)


class ClientType(models.Model):
    client_type_name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)


class Role(models.Model):
    role_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class Module(models.Model):
    module_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class ActionType(models.Model):
    action_type = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class VirtualAgentType(models.Model):
    virtual_agent_type = models.CharField(max_length=50)
    description = models.TextField(max_length=500)


class Function(models.Model):
    function_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=False)


__all__ = [
    "Country",
    "ClientType",
    "Role",
    "Module",
    "ActionType",
    "VirtualAgentType",
    "Function",
]
