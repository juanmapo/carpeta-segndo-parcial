import pygame
from random import randint

class Enemigo:
    def __init__(self) -> None:
        self.enemigo_png = pygame.image.load("nave_enemiga.png")
        self.enemigo_png = pygame.transform.scale(self.enemigo_png,(50,50))
        self.rectangulo = self.enemigo_png.get_rect()
        self.lista_disparos = []
        self.rectangulo.x  = randint(0,1080)
        self.rectangulo.y  = randint(0,400)
        self.velocidad_x = 2
        self.velocidad_y = 2
        self.vida = 1
        
        self.sonido_explosion = pygame.mixer.Sound('explosion.wav')
        self.sonido_disparo = pygame.mixer.Sound('sonido_laser.mp3')
        
    
    
    def dibujar(self,pantalla):
        pantalla.blit(self.enemigo_png,self.rectangulo)
    
    def ataque(self,x,y):
        if(randint(0,100)<1):
            x += 12
            self.disparo(x,y)
            self.sonido_disparo.play()
    
    def disparo(self,x,y):
        self.proyectil = Proyectil(x,y)
        self.lista_disparos.append(self.proyectil)
        
    def movimineto(self):
        self.rectangulo.x -= self.velocidad_x
        self.rectangulo.y -= self.velocidad_y
        
        if self.rectangulo.x < 0:
            self.velocidad_x = -3
        
        if self.rectangulo.x > 1000:
            self.velocidad_x = 3
        
        if self.rectangulo.y < 0:
            self.velocidad_y = -2
        
        if self.rectangulo.y > 500:
            self.velocidad_y = 2

class Proyectil:
    def __init__(self,posx,posy) -> None:
        self.imagen_proyectil = pygame.image.load("bala_enemiga.png")
        self.rectangulo_proyectil = self.imagen_proyectil.get_rect()
        self.rectangulo_proyectil.y = posy
        self.rectangulo_proyectil.x = posx
        self.velocidad_proyectil = 4
        

    def trayectoria(self):
        self.rectangulo_proyectil.y = self.rectangulo_proyectil.y + self.velocidad_proyectil
    
    def dibujar(self,superficie):
        superficie.blit(self.imagen_proyectil,self.rectangulo_proyectil)