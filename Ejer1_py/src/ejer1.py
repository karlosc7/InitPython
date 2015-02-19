# -*- coding: utf-8 -*-
'''
Created on 22/01/2015

@author: karlosc
'''

#Cambios del programa 1
#El encoding le cambio al principio del programa
#Le hago un cast con int "como bien me decías"
print 'Programa que calcula el perímetro y el área de un rectángulo'

x = int(raw_input("Introduce el valor de un lado x del rectángulo: "))

y = int(raw_input("Introduce el valor de un lado y del rectángulo: "))

#Cambios en la fórmula del perímetro
perimetro = 2*x + 2*y 
print "El perímetro del rectángulo es:", perimetro, "metros"
area = x * y
print "El área del rectángulo es:", area, "metros^2"
