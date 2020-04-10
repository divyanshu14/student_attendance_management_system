from django.apps import AppConfig
from . import signals

class DatabaseManagerConfig(AppConfig):
    name = 'database_manager'
    def ready(self):
        import signals