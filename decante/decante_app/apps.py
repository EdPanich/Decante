from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

class DecanteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'decante_app'

    def ready(self):
        from django.contrib.auth.models import User
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@decante.com',
                    password='admin123'
                )
        except OperationalError:
            pass  # Para evitar error en primera migración
