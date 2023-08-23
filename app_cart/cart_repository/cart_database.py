from configuration.database import connection

# with connection.cursor() as cursor:
#     cursor.execute('SELECT * from cart;')
#     col_names = [desc[0] for desc in cursor.description]
#     print(col_names)


def cart_db(grpc_data):
    with connection.cursor() as cursor:
        data = grpc_data.message
        cursor.execute(f"insert into cart (prod_name) values ('{data}');")
        connection.commit()
        return ''
