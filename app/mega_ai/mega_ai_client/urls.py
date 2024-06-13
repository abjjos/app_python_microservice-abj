from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActionDetailViewSet,
    ClientModuleViewSet,
    ClientSubscriptionViewSet,
    ClientViewSet,
    GoalDetailViewSet,
    GoalTypeViewSet,
    ProjectViewSet,
    ReportViewSet,
    UserViewSet,
    VirtualAgentDetailsViewSet,
)

router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"client-subscriptions", ClientSubscriptionViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"users", UserViewSet)
router.register(r"client-modules", ClientModuleViewSet)
router.register(r"goal-types", GoalTypeViewSet)
router.register(r"goal-details", GoalDetailViewSet)
router.register(r"action-details", ActionDetailViewSet)
router.register(r"virtual-agent-details", VirtualAgentDetailsViewSet)
router.register(r"reports", ReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
