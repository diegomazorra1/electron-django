import serial
import time

ser=serial.Serial('COM8', baudrate= 9600, timeout=1)
time.sleep(3)
numPoints= 4
datalist= [0]*numPoints
dataFile= open('dataFile.txt', 'w')

def getValues():

    ser.write(b'g')
    arduinoData=ser.readline().decode().split('\r\n')

    return arduinoData[0]


while (1):

    userInput= input('Get data points?')

    if userInput=='y' :
       for i in range(0,numPoints) :

           data=getValues()
           dataFile.write(data + ' ')
           datalist[i]= data
           Nombre=datalist[1]
           Uid=datalist[2]
           Saldo=datalist[3]




       print(type(data))

       print('Nombre = ' + str(Nombre))
       print('Uid = ' + str(Uid))
       print('Saldo Actual = ' + str(Saldo))


       print(datalist)
       dataFile.close()
       break
