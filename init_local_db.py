import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'STMS.settings')
django.setup()

def init_local_db():
    try:
        # Crear migraciones
        os.system('python manage.py makemigrations')
        
        # Aplicar migraciones
        os.system('python manage.py migrate')
        
        # Crear superusuario
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                user_type='admin',
                phone='',
                address=''
            )
            print("Superusuario creado exitosamente")
        else:
            print("El superusuario ya existe")
            
        print("Base de datos local inicializada correctamente")
        
    except Exception as e:
        print(f"Error al inicializar la base de datos: {str(e)}")
        raise

if __name__ == "__main__":
    init_local_db() 