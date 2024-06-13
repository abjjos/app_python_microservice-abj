from rest_framework import serializers

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


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSubscription
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ClientModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModule
        fields = "__all__"


class GoalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalType
        fields = "__all__"


class GoalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalDetail
        fields = "__all__"


class ActionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionDetail
        fields = "__all__"


class VirtualAgentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualAgentDetails
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
