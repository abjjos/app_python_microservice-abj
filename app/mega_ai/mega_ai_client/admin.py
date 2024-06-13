from django.contrib import admin

from .models import (
    ActionDetail,
    Client,
    ClientModule,
    ClientSubscription,
    GoalDetail,
    GoalType,
    Project,
    Report,
    User,
    VirtualAgentDetails,
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "client_name",
        "is_active",
        "created_at",
        "updated_at",
        "country_id",
        "client_type_id",
    )
    search_fields = ("client_name",)
    list_filter = ("is_active", "country_id", "client_type_id")
    ordering = ("client_name",)


@admin.register(ClientSubscription)
class ClientSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("client_id", "status", "next_billing_date", "comments")
    search_fields = ("client_id__client_name",)
    list_filter = ("status",)
    ordering = ("client_id",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "client_id", "is_active")
    search_fields = ("project_name", "client_id__client_name")
    list_filter = ("is_active",)
    ordering = ("project_name",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "user_email",
        "client_id",
        "role_id",
        "country_id",
        "created_at",
        "updated_at",
    )
    search_fields = ("user_name", "user_email", "client_id__client_name")
    list_filter = ("role_id", "country_id")
    ordering = ("user_name",)


@admin.register(ClientModule)
class ClientModuleAdmin(admin.ModelAdmin):
    list_display = ("client_id", "module_id", "is_enabled")
    search_fields = ("client_id__client_name", "module_id__name")
    list_filter = ("is_enabled",)
    ordering = ("client_id",)


@admin.register(GoalType)
class GoalTypeAdmin(admin.ModelAdmin):
    list_display = ("goal_type_name", "module_id", "description")
    search_fields = ("goal_type_name", "module_id__name")
    ordering = ("goal_type_name",)


@admin.register(GoalDetail)
class GoalDetailAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "goal_type_id",
        "goal_reached_when",
        "special_goals_logic",
        "comments",
    )
    search_fields = ("client_id__client_name", "goal_type_id__goal_type_name")
    ordering = ("client_id",)


@admin.register(ActionDetail)
class ActionDetailAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "action_type_id",
        "action_destination_details",
        "action_connection_details",
        "action_response_log_details",
        "description",
    )
    search_fields = ("client_id__client_name", "action_type_id__name")
    ordering = ("client_id",)


@admin.register(VirtualAgentDetails)
class VirtualAgentDetailsAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "virtual_agent_type_id",
        "external_ref_id",
        "external_bot_id",
        "external_ref_details",
    )
    search_fields = ("client_id__client_name", "virtual_agent_type_id__name")
    ordering = ("client_id",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "report_details",
        "description",
        "created_at",
        "updated_at",
    )
    search_fields = ("client_id__client_name",)
    ordering = ("client_id",)
