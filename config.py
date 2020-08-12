import psycopg2

# conexion a la BD
class conexion:
    @staticmethod
    def conect_post():
        try:
            connection = psycopg2.connect(
                database="central2010", user="postgres", password="atentusdesa", host="172.16.5.117", port="5432")
            cursor = connection.cursor()
            return cursor
        except:
            return False
