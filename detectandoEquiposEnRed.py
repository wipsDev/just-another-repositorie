#!/usr/bin/python
import commands


print commands.getoutput('sudo nmap -sP 192.168.1.1-254')

print ""
print "Responden las siguientes ips :"
print ""


Base = commands.getoutput('sudo nmap -sP 192.168.1.1-254')


## Obteniendo hora y dia

Proc= Base.split("UTC")
Proc=Proc[0].split("at ")
HoraYdia=Proc[1]
print HoraYdia



## Obteniendo Dispositivos encontrados


Proc=Base.split("Nmap done: 254 IP addresses (")
FraseFinal = Proc[1].split(' hosts up) scanned in ')
#Aqui dividimos para llegar a los dos parametros de la frase final

##Numero de dispositivos
DispEncontrados= FraseFinal[0]

print "Se han encontrado " + DispEncontrados+ " dispositivos conectados"


## Tiempo de procesamiento
print "Tiempo en escanear " + FraseFinal[1]


##Tratamiento del Grueso de datos

##Quitamos los extremos superior e inferior

Datos = Base.split("UTC")
Datos = Datos[1].split("Nmap done")


## Datos aislados

SoloDatosDeDispositivos = Datos[0].split("Nmap scan report for ")

## Modificamos este valor para cambiar entre las diferentes ips



NumeroDeEquiposContectados = len(SoloDatosDeDispositivos)


## El -1 es para que no coga el 0
Lista=range(NumeroDeEquiposContectados-1)



for x in range (1,NumeroDeEquiposContectados-1):
    Datos = SoloDatosDeDispositivos[x]

##    print "--------------------------"


    Datos = Datos.split('Host is up ')

    Ip = Datos[0].strip()
##    print Ip

    MacAdress = Datos[1].split("MAC Address: ")
    Latencia = MacAdress[0].split()

    Latencia= Latencia[0].replace("(","")
##    print Latencia

    MacAdress1 = MacAdress[1].split()

    MacAdress = MacAdress1[0]

##    print MacAdress


    MarcaDelDispositivo = MacAdress1[1]
##    print MarcaDelDispositivo

    
    Lista[x-1]=(Ip,Latencia,MacAdress,MarcaDelDispositivo)



for x in Lista:
    print x







