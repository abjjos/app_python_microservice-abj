from django.contrib import admin

from .models import (
    ActionType,
    ClientType,
    Country,
    Function,
    Module,
    Role,
    VirtualAgentType,
)

admin.site.register(Country)
admin.site.register(ClientType)
admin.site.register(Role)
admin.site.register(Module)
admin.site.register(ActionType)
admin.site.register(VirtualAgentType)
admin.site.register(Function)
