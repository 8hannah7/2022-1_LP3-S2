# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:03:16 2022

@author: roxana
"""
#importamos la libreria
import camelcase
nombre = "roxana condori condori"
print(nombre.upper())
print(nombre.title())
#creamos un objeto llamado cam
cam=camelcase.CamelCase()
print("con camelcase ....")

#imprimimos el nombre en formato titulo
#utilizamos camelcase

print(cam.hump(nombre))

#para resolver el proeblema
#creamos otro objeto llamado cam2
# 'roxana' y 'condori'

cam2=camelcase.CamelCase('roxana', 'condori')
print(cam2.hump(nombre))