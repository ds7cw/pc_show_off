from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pc_show_off.accounts'

    def ready(self):
        import pc_show_off.accounts.signals
