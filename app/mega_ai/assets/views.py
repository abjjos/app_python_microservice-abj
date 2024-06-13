from rest_framework import viewsets

from .models import (
    ActionType,
    ClientType,
    Country,
    Function,
    Module,
    Role,
    VirtualAgentType,
)
from .serializers import (
    ActionTypeSerializer,
    ClientTypeSerializer,
    CountrySerializer,
    FunctionSerializer,
    ModuleSerializer,
    RoleSerializer,
    VirtualAgentTypeSerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ClientTypesViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ActionTypesViewSet(viewsets.ModelViewSet):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer


class VirtualAgentTypesViewSet(viewsets.ModelViewSet):
    queryset = VirtualAgentType.objects.all()
    serializer_class = VirtualAgentTypeSerializer


class FunctionsViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
