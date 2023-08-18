import psycopg2

connection = psycopg2.connect(
    host='172.17.0.2',
    database='my_shop',
    user='sergey',
    password='12345',
    port='5432'
)

# cursor = connection.cursor()
# cursor.execute('select version();')
# print(cursor.fetchall())
