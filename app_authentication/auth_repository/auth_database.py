from configuration.database import connection

with connection.cursor() as cursor:
    cursor.execute('SELECT * from auth;')
    col_names = [desc[0] for desc in cursor.description]
    print(col_names)
