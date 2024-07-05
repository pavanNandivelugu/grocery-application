import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='Mywishes@789',
                              host='127.0.0.1', database='Grocery store',
                              auth_plugin='mysql_native_password')
    return __cnx