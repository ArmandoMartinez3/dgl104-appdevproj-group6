import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'STMS.settings')
django.setup()

def create_superuser():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'cheetos123')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            user_type='admin'
        )
        print(f"Superusuario {username} creado exitosamente")
    else:
        print(f"El superusuario {username} ya existe")

if __name__ == "__main__":
    create_superuser() 