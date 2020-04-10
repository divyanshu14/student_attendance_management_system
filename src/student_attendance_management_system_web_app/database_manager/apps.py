from django.apps import AppConfig


class DatabaseManagerConfig(AppConfig):
    name = 'database_manager'
    def ready(self):
        import database_manager.signals
