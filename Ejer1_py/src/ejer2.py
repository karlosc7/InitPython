# -*- coding: utf-8 -*-
'''
Created on 22/01/2015

@author: karlosc
'''

#Cambio a la primera línea el encoding
#Creamos un almacén de notas
Notas = []
#Inicializo el contador de las notas a introducir a cero
cont = 0
#Notas que vamos a ingresar hasta que ingresemos -1 para salir 
while cont != -1:
    cont= int(raw_input("Ingresa la nota: ")) 
    #Si la nota no está entre 1 y 10 no es válido 
    if cont != -1 and (cont < 0 or cont > 10):
        print "Número incorrecto, introduzca uno válido o -1 para salir"
    elif cont >= 0 and cont <= 10:
        Notas.append(cont)

#hemos salido del bucle
#Contador del número de notas introducidas 
xrec = len(Notas)
iAprobados = 0
if xrec > 0:
    for i in Notas:
        #Sumatorio de aprobados
        if i >= 5: 
            iAprobados += 1
    #Muestro los porcentajes de aprobados y suspensos
    print "El porcentaje de aprobados es:", iAprobados * 100 / xrec, "%"
    print "el porcentaje de suspensos es:", (xrec - iAprobados) * 100 / xrec, "%"

else :
    print "no hay calificaciones"
    



