from datetime import datetime

from assets.models import (
    ActionType,
    ClientType,
    Country,
    Module,
    Role,
    VirtualAgentType,
)
from django.core.management.base import BaseCommand
from mega_ai_client.models import (
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


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        self.seed_data()
        self.stdout.write("Data seeded successfully.")

    def seed_data(self):
        # Create Country
        country = Country.objects.create(name="USA", phone_extension="+1")

        # Create ClientType
        client_type = ClientType.objects.create(
            client_type_name="Premium", description="Premium client type"
        )

        # Create Client
        client = Client.objects.create(
            client_name="Test Client",
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            country_id=country,
            client_type_id=client_type,
        )

        # Create Role
        role = Role.objects.create(role_name="Admin", description="Admin role")

        # Create ClientSubscription
        ClientSubscription.objects.create(
            client_id=client,
            status=1,
            next_billing_date=datetime.now(),
            comments="Initial subscription",
        )

        # Create Project
        Project.objects.create(
            client_id=client,
            project_name="Test Project",
            description="This is a test project",
            is_active=True,
        )

        # Create User
        User.objects.create(
            client_id=client,
            role_id=role,
            user_type_id=client_type,
            country_id=country,
            user_name="testuser",
            user_email="testuser@example.com",
            password_hash="hashedpassword",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        # Create Module
        module = Module.objects.create(
            module_name="Test Module", description="This is a test module"
        )

        # Create ClientModule
        ClientModule.objects.create(client_id=client, module_id=module, is_enabled=True)

        # Create GoalType
        goal_type = GoalType.objects.create(
            module_id=module,
            goal_type_name="Test Goal Type",
            description="This is a test goal type",
        )

        # Create GoalDetail
        GoalDetail.objects.create(
            client_id=client,
            goal_type_id=goal_type,
            goal_reached_when="Test goal reached when",
            special_goals_logic="Test special goals logic",
            comments="Test comments",
        )

        # Create ActionType
        action_type = ActionType.objects.create(
            action_type="Test Action Type", description="This is a test action type"
        )

        # Create ActionDetail
        ActionDetail.objects.create(
            client_id=client,
            action_type_id=action_type,
            action_destination_details="Test action destination details",
            action_connection_details="Test action connection details",
            action_response_log_details="Test action response log details",
            description="Test action description",
        )

        # Create VirtualAgentType
        virtual_agent_type = VirtualAgentType.objects.create(
            virtual_agent_type="Test Virtual Agent Type",
            description="This is a test virtual agent type",
        )

        # Create VirtualAgentDetails
        VirtualAgentDetails.objects.create(
            client_id=client,
            virtual_agent_type_id=virtual_agent_type,
            external_ref_id="Test external ref id",
            external_bot_id="Test external bot id",
            external_ref_details="Test external ref details",
        )

        # Create Report
        Report.objects.create(
            client_id=client,
            report_details="Test report details",
            description="Test report description",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
