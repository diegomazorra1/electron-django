
import psycopg2

try:
  conn_string="dbname='SASRU' user='postgres' host='localhost' password='ingenieria@'"
  print ("Connecting to database\n->%s" % (conn_string))

  conn = psycopg2.connect(conn_string)
  print ("connection succeeded")
except:
  print ("no connection to db")

cur = conn.cursor()

#cur.execute("select id from usuarios_usuario")
# realizo consulta a usuario especifico
cur.execute("select * from usuarios_usuario where id=%s",(21,))

#------- seleccionar unas columnas

rows = cur.fetchone()

# imprimir filas

print(rows)
"""

for row in rows:
    print( "   ", row[0])
    """
   
conn.close()
