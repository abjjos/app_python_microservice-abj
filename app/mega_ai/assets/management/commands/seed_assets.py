from assets.models import (
    ActionType,
    ClientType,
    Country,
    Function,
    Module,
    Role,
    VirtualAgentType,
)
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        self.create_client_types()
        self.create_roles()
        self.create_modules()
        self.create_action_types()
        self.create_virtual_agent_types()
        self.stdout.write("Data seeded successfully.")

    def create_countries(self):
        countries_data = [
            {"name": "Denmark", "description": "+45"},
            {"name": "Canada", "description": "+1"},
        ]
        for data in countries_data:
            Country.objects.create(**data)

    def create_client_types(self):
        client_types_data = [
            {"client_type_name": "Corporate", "description": "Corporate clients"},
            {"client_type_name": "Individual", "description": "Individual clients"},
        ]
        for data in client_types_data:
            ClientType.objects.create(**data)

    def create_roles(self):
        roles_data = [
            {"role_name": "Admin", "description": "Administrator role"},
            {"role_name": "User", "description": "Regular user role"},
        ]
        for data in roles_data:
            Role.objects.create(**data)

    def create_modules(self):
        modules_data = [
            {"module_name": "Authentication", "description": "Authentication module"},
            {"module_name": "Billing", "description": "Billing module"},
        ]
        for data in modules_data:
            Module.objects.create(**data)

    def create_action_types(self):
        action_types_data = [
            {"action_type": "Login", "description": "User login action"},
            {"action_type": "Purchase", "description": "Purchase action"},
        ]
        for data in action_types_data:
            ActionType.objects.create(**data)

    def create_virtual_agent_types(self):
        virtual_agent_types_data = [
            {"virtual_agent_type": "Chatbot", "description": "Chatbot type"},
            {
                "virtual_agent_type": "Voice Assistant",
                "description": "Voice Assistant type",
            },
        ]
        for data in virtual_agent_types_data:
            VirtualAgentType.objects.create(**data)

    def create_functions(self):
        functions_data = [
            {
                "function_name": "function1",
                "description": "Chatbot function",
                "is_active": False,
            },
            {
                "function_name": "function2",
                "description": "Voice Assistant function",
                "is_active": False,
            },
        ]
        for data in functions_data:
            Function.objects.create(**data)
