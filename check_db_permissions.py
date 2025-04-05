import os
import psycopg2
from urllib.parse import urlparse

def check_database_permissions():
    try:
        # Obtener la URL de la base de datos del entorno
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            print("Error: DATABASE_URL no está definida en las variables de entorno")
            return False

        # Parsear la URL de la base de datos
        parsed_url = urlparse(database_url)
        
        # Establecer conexión
        conn = psycopg2.connect(
            dbname=parsed_url.path[1:],
            user=parsed_url.username,
            password=parsed_url.password,
            host=parsed_url.hostname,
            port=parsed_url.port
        )
        
        # Crear un cursor
        cur = conn.cursor()
        
        # Verificar permisos de lectura
        cur.execute("SELECT 1")
        print("✓ Permisos de lectura verificados")
        
        # Verificar permisos de escritura
        cur.execute("CREATE TEMP TABLE test_permissions (id integer)")
        cur.execute("INSERT INTO test_permissions VALUES (1)")
        cur.execute("DROP TABLE test_permissions")
        print("✓ Permisos de escritura verificados")
        
        # Verificar permisos de creación de tablas
        cur.execute("""
            SELECT has_table_privilege(current_user, 'gymapp_customuser', 'SELECT')
        """)
        print("✓ Permisos de acceso a tablas verificados")
        
        cur.close()
        conn.close()
        print("✓ Todas las verificaciones completadas exitosamente")
        return True
        
    except Exception as e:
        print(f"Error al verificar permisos: {str(e)}")
        return False

if __name__ == "__main__":
    check_database_permissions() 