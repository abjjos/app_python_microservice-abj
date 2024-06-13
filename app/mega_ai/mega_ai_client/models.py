from assets.models import (
    ActionType,
    ClientType,
    Country,
    Module,
    Role,
    VirtualAgentType,
)
from django.db import models
from django.utils import timezone


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    disabled_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField()
    country_id = models.ForeignKey(Country, on_delete=models.RESTRICT)
    client_type_id = models.ForeignKey(ClientType, on_delete=models.RESTRICT)


class ClientSubscription(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.IntegerField()
    next_billing_date = models.DateTimeField()
    comments = models.TextField(max_length=255)


class Project(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    is_active = models.BooleanField(default=False)


class User(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_type_id = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()


class ClientModule(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=False)


class GoalType(models.Model):
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    goal_type_name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)


class GoalDetail(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    goal_type_id = models.ForeignKey(GoalType, on_delete=models.CASCADE)
    goal_reached_when = models.CharField(max_length=100)
    special_goals_logic = models.CharField(max_length=255)
    comments = models.TextField(max_length=255)


class ActionDetail(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    action_type_id = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    action_destination_details = models.CharField(max_length=255)
    action_connection_details = models.CharField(max_length=255)
    action_response_log_details = models.TextField(max_length=255)
    description = models.TextField(max_length=255)


class VirtualAgentDetails(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    virtual_agent_type_id = models.ForeignKey(
        VirtualAgentType, on_delete=models.CASCADE
    )
    external_ref_id = models.CharField(max_length=50)
    external_bot_id = models.CharField(max_length=50)
    external_ref_details = models.CharField(max_length=255)


class Report(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    report_details = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()


__all__ = [
    "Client",
    "ClientSubscription",
    "Project",
    "User",
    "ClientModule",
    "GoalType",
    "GoalDetail",
    "ActionDetail",
    "VirtualAgentDetails",
    "Report",
]
