from configuration.database import connection

# with connection.cursor() as cursor:
#     cursor.execute('SELECT * from shop;')
#     col_names = [desc[0] for desc in cursor.description]
#     print(col_names)
#     cursor.execute('SELECT * from category;')
#     col_names = [desc[0] for desc in cursor.description]
#     print(col_names)


def shop_db():
    with connection.cursor() as cursor:
        data_str = str()
        cursor.execute('SELECT prod_name, count, price from shop;')
        data = cursor.fetchall()
        for tup in data:
            for string in tup:
                data_str += str(string) + ' '
            data_str += '\n'
        return data_str


# print(shop_db())
