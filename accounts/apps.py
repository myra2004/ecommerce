from django.apps import AppConfig
from django.core.signals import setting_changed


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        pass