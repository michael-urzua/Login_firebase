from config import conexion
import psycopg2
import psycopg2.extras
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class consulta_inicial:
    @staticmethod
    def select_inicial():
        try:
            cursor = conexion.conect_post()
            cursor.execute("""SELECT
                                	re.objetivo_id,
                                	re.objetivo_nombre,
                                	re.paso_nombre,
                                	cau.causa_nombre,
                                	inci.incidencia_nombre,
                                	re.fecha_inicial :: TIMESTAMP,
                                	re.fecha_final :: TIMESTAMP,
                                	cate.categoria_nombre
                                FROM
                                	sbif.registro re
                                INNER JOIN sbif.causa cau ON re.causa_id = cau.causa_id
                                INNER JOIN sbif.incidencia inci ON inci.incidencia_id = re.incidencia_id
                                INNER JOIN sbif.categoria cate ON cate.categoria_id = re.categoria_id
                                WHERE
                                	re.fecha_inicial::date BETWEEN '2020-07-01' and '2020-07-31' """)

            return cursor
        except:
            return False
