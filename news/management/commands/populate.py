from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from news.library import ADMIN_GROUP_NAME, EDITOR_GROUP_NAME, USER_GROUP_NAME, premoderate_codename
from news.models import Post, User
from news.library import fixtures


class Command(BaseCommand):
    admin_group_key = 'admin_group'
    editor_group_key = 'editor_group'
    user_group_key = 'user_group'

    def handle(self, *args, **options):
        groups = self.__create_groups()
        self.__create_custom_permission(groups)
        self.__create_users()

    def __create_groups(self):
        admin_group, created = Group.objects.get_or_create(name=ADMIN_GROUP_NAME)
        editor_group, created = Group.objects.get_or_create(name=EDITOR_GROUP_NAME)
        user_group, created = Group.objects.get_or_create(name=USER_GROUP_NAME)
        return {
            self.admin_group_key: admin_group,
            self.editor_group_key: editor_group,
            self.user_group_key: user_group
        }

    def __create_custom_permission(self, groups):
        ct = ContentType.objects.get_for_model(Post)
        permission = Permission.objects.create(codename=premoderate_codename,
                                               name='Can post without premoderation',
                                               content_type=ct)
        groups.get(self.user_group_key).permissions.add(permission)
        groups.get(self.editor_group_key).permissions.add(permission)

    def __create_users(self):
        User.objects.create_admin(**fixtures.users.get('admin'))
        User.objects.create_editor(**fixtures.users.get('editor'))
        User.objects.create_user(**fixtures.users.get('user'))
