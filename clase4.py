import pygame

def get_imagenes(path,filas,columnas):
    lista = []
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)
    
    for fila in range(filas):
        for columna in range(columnas):
            x = columna + fotograma_ancho
            y = fila + fotograma_alto
            supeficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            lista.append(supeficie_fotograma)
    return lista


class Personaje:
    def __init__(self) -> None:
        self.caminar =get_imagenes("imagen",1,3)
        self.paso1 = 0
        self.score = 0
        self.animacion = self.caminar
        self.imagen = self.animacion[self.paso1]
        self.rect = self.imagen.get_rect()
        self.rect.y = 500
        
    def actualizar(self):
        if(self.paso1 < len(self.animacion)- 1):
            self.paso1 +=1
        else:
            self.paso1 = 0
    def dibujar(self,pantalla):
        self.imagen = self.animacion[self.paso1]
        pantalla.vlit(self.imagen,self.rect)





alto_ventana = 1920
ancho_ventana = 1000


pygame.init()

screen = pygame.display.set_mode((alto_ventana,ancho_ventana))
pygame.display.set_caption("parcialito games")


osito = Personaje()

bandera_progama_corriendo = True
while bandera_progama_corriendo:
    lista_de_eventos = pygame.event.get()
    for evento in lista_de_eventos:
        if evento.type == pygame.QUIT:
            bandera_progama_corriendo = False 



pygame.quit()