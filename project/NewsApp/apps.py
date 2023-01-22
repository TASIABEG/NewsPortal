from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewsApp'

    def ready(self):
        import NewsApp.signals