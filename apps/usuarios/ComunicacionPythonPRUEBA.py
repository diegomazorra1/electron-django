

import serial
import psycopg2

UID_1='CB179C9'

def consulta(UID):
        if UID == UID_1:
                print ("ACCESO CONCEDIDO")
        


# conexion a la base de datos-----------

try:
  conn_string="dbname='SASRU' user='postgres' host='localhost' password='ingenieria@'"
  print ("Connecting to database\n->%s" % (conn_string))

  conn = psycopg2.connect(conn_string)
  print ("connection succeeded")
except:
  print ("no connection to db")

cur = conn.cursor()


                    

#---------------------------------------------------------




arduino = serial.Serial('COM8',9600, timeout=.1)
while True:
        #ELIMNAR CARACTERES DE NUEVA LINEA DE Serial.println de Arduino
   
        data = arduino.readline()[:-2]
        data = data.decode("utf-8")
##        print(data)
            
        if data:
            """
            print (data)
            print (type(data))
            print (len(data))
            """
            if 'UID' in data:
                    UID = data[4:]
                    print ("llego el identificador", UID)
                    
            if 'Name' in data:
                    Nombre = data[5:]
                    print ("llego el Nombre", Nombre)
            if 'Saldo' in data:
                    Saldo = data[7:]
                    print ("llego el SALDO", Saldo )
                    print (type(Saldo))


                    Saldo_str = str(Saldo)

                    print(UID)
                    print (type(UID))

                    
                    
                    Saldo_int = int(Saldo_str)
                    
                    cur.execute("select * FROM usuarios_usuario WHERE uid = %s ",(Saldo,))
                    rows = cur.fetchone()
                    print(rows)
                    
                    



            consulta(UID)
                    

       
        else:
            print ("no hay datos")


conn.close()           

