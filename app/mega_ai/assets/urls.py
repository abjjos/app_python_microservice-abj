from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActionTypesViewSet,
    ClientTypesViewSet,
    ModulesViewSet,
    RolesViewSet,
    VirtualAgentTypesViewSet,
)

router = DefaultRouter()
router.register(r"client-types", ClientTypesViewSet)
router.register(r"roles", RolesViewSet)
router.register(r"modules", ModulesViewSet)
router.register(r"action-types", ActionTypesViewSet)
router.register(r"virtual-agent-types", VirtualAgentTypesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
