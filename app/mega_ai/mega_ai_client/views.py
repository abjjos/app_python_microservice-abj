from rest_framework import viewsets

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
from .serializers import (
    ActionDetailSerializer,
    ClientModuleSerializer,
    ClientSerializer,
    ClientSubscriptionSerializer,
    GoalDetailSerializer,
    GoalTypeSerializer,
    ProjectSerializer,
    ReportSerializer,
    UserSerializer,
    VirtualAgentDetailsSerializer,
)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientModuleViewSet(viewsets.ModelViewSet):
    queryset = ClientModule.objects.all()
    serializer_class = ClientModuleSerializer


class GoalTypeViewSet(viewsets.ModelViewSet):
    queryset = GoalType.objects.all()
    serializer_class = GoalTypeSerializer


class GoalDetailViewSet(viewsets.ModelViewSet):
    queryset = GoalDetail.objects.all()
    serializer_class = GoalDetailSerializer


class ActionDetailViewSet(viewsets.ModelViewSet):
    queryset = ActionDetail.objects.all()
    serializer_class = ActionDetailSerializer


class VirtualAgentDetailsViewSet(viewsets.ModelViewSet):
    queryset = VirtualAgentDetails.objects.all()
    serializer_class = VirtualAgentDetailsSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
