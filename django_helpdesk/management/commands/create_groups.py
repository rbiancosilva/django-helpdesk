from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create default groups with permissions'

    def handle(self, *args, **kwargs):
        groups_permissions = {
            'operator': ['view_ticket', 'change_ticket', 'change_article', 'change_profile'],  # Example permissions
            'user': ['view_ticket', 'add_ticket', 'change_ticket', 'change_profile']  # Example permissions
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                permissions = Permission.objects.filter(codename__in=perms)
                group.permissions.set(permissions)
                group.save()
                self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created with permissions.'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" already exists.'))
