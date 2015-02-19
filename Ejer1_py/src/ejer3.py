# -*- coding: utf-8 -*-
'''
Created on 22/01/2015

@author: karlosc
'''
# Declaramos billetes y monedas (euros) en forma de tupla
pMonedas = (200, 100, 50, 20, 10, 2, 1)
sMonedas = [0, 0, 0, 0, 0, 0, 0]

#Pido al usuario la cantidad
iNumero = -1
while iNumero < 0:
    iNumero = int(raw_input("Introduzca una cantidad de euros"))
    
    
# De esta manera podemos conseguir los billetes y monedas
i = 0
while iNumero > 0:
    if iNumero >= pMonedas[i]:
        sMonedas[i] += 1
        iNumero -= pMonedas[i]
    else:
        i += 1
        
#ahora recorremos el resultado
print sMonedas
i = 0
for iBillete in sMonedas:
    if iBillete > 0:
        #No me muestra bien la cantidad de cada valor de billetes y monedas
        print "Tienes %d de %d", sMonedas[i], pMonedas[i]
    i += 1