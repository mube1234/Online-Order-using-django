from django.apps import AppConfig


class AbmublogConfig(AppConfig):
    name = 'abmublog'
    def ready(self):
        import abmublog.signals
