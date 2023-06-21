import pygame



class Nave_pj:
    def __init__(self,) -> None:
        self.vida = 3
        self.nave_png = pygame.image.load("nave.png")
        self.imagen_nave = pygame.transform.scale(self.nave_png,(100,100))
        self.rectangulo = self.imagen_nave.get_rect()
        self.rectangulo.x = 480
        self.rectangulo.y = 600
        self.hitbox_horizontal = pygame.Rect(480,610,24,80)
        self.hitbox_vertical = pygame.Rect(480,674,96,10)
        
        
        
        self.torreta = pygame.image.load("torreta.png")
        self.imagen_torreta = pygame.transform.scale(self.torreta,(30,30))
        self.rect_torreta = self.torreta.get_rect()
        self.listaDisparos = []
        
        self.sonido_disparo = pygame.mixer.Sound('sonido_laser.mp3')
        
    def dibujar(self,pantalla):
        self.hitbox_horizontal.x = self.rectangulo.x + 38
        
        self.hitbox_vertical.x = self.rectangulo.x + 2
        
        self.rect_torreta.x = self.rectangulo.x + 35
        self.rect_torreta.y = self.rectangulo.y + 43
        
        pantalla.blit(self.imagen_nave,self.rectangulo)
        pantalla.blit(self.imagen_torreta,self.rect_torreta)
        
    def disparar(self,x,y):
        proyectil = Proyectil(x,y)
        self.listaDisparos.append(proyectil)
        self.sonido_disparo.play()

class Proyectil:
    def __init__(self,posx,posy) -> None:
        self.imagen_proyectil = pygame.image.load("bala_violeta.png")
        self.rectangulo_proyectil = self.imagen_proyectil.get_rect()
        self.rectangulo_proyectil.y = posy
        self.rectangulo_proyectil.x = posx
        self.velocidad_proyectil = 5
        

    def trayectoria(self):
        self.rectangulo_proyectil.y = self.rectangulo_proyectil.y - self.velocidad_proyectil
    
    def dibujar(self,superficie):
        superficie.blit(self.imagen_proyectil,self.rectangulo_proyectil)
        








