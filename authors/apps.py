from django.apps import AppConfig


class AuthorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authors"

    def ready(self, *args, **kwargs):
        import authors.signals
        return super().ready(*args, **kwargs)