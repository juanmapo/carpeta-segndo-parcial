import pygame


def calcuar_centro(tupla):
    bandera = True
    for posicion in tupla:
        if bandera:
            bandera = False
            x = posicion + 38
        else:
            y = posicion + 15
            return x,y

posicion_nave = (30,550)


calcuar_centro(posicion_nave)


