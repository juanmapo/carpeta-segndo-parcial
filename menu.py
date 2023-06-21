import pygame
import sys
import pygame_gui
from nave_principal import Nave_pj
from Enemigos import Enemigo 
import sqlite3
from rankings import * 
import colores


pygame.init()

class Boton():
    def __init__(self,imagen,x,y,imagen_presionda,pantalla):
        self.imagen = imagen
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.pantalla = pantalla
        
        self.imagen_presionda = imagen_presionda
        
        
    def dibujar(self):
        self.pantalla.blit(self.imagen,self.rectangulo)
        
    def revisar_input(self,posicion):
        if posicion[0] in range(self.rectangulo.left,self.rectangulo.right) and posicion[1] in range(self.rectangulo.top,self.rectangulo.bottom): 
            return True
        
    def cambiar_color(self,posicion,):
        if posicion[0] in range(self.rectangulo.left,self.rectangulo.right) and posicion[1] in range(self.rectangulo.top,self.rectangulo.bottom): 
            self.pantalla.blit(self.imagen_presionda,(self.rectangulo.x,self.rectangulo.y))

def main_menu(pantalla):
    pygame.display.set_caption("menu")
    fondo =  pygame.image.load("fondo.jpg")
    fondo = pygame.transform.scale(fondo,(1080,720))
    
    boton_salir_png = pygame.image.load("boton_salir.png")
    boton_salir_presionado_png = pygame.image.load("boton_salir_presionado.png")
    boton_salir = Boton(boton_salir_png,450,420,boton_salir_presionado_png,pantalla)
    
    boton_rankings_png = pygame.image.load("boton_rankings.png")
    boton_rankings_presionado_png = pygame.image.load("boton_rankings_presionado.png")
    boton_rankings = Boton(boton_rankings_png,450,310,boton_rankings_presionado_png,pantalla)
    
    boton_jugar_png = pygame.image.load("boton_jugar.png")
    boton_jugar_presionado_png = pygame.image.load("boton_jugar_presionado.png")
    boton_jugar = Boton(boton_jugar_png,450,200,boton_jugar_presionado_png,pantalla)
    
    musica_menu = pygame.mixer.Sound('musica_menu.mp3')
    musica_menu.set_volume(0.5)
    musica_menu.play(-1)
    
    flag_correr = True
    while flag_correr:
        
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_correr = False
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_salir.revisar_input(pygame.mouse.get_pos()):
                    flag_correr = False
                    pygame.quit()
                    sys.exit()
                if boton_jugar.revisar_input(pygame.mouse.get_pos()):
                    musica_menu.stop()
                    jugar()

                if boton_rankings.revisar_input(pygame.mouse.get_pos()):
                    puntuaciones(pantalla)
                    
        
        pantalla.blit(fondo,(0,0))
        
        boton_jugar.dibujar()
        boton_jugar.cambiar_color(pygame.mouse.get_pos())
        
        boton_rankings.dibujar()
        boton_rankings.cambiar_color(pygame.mouse.get_pos())
        
        boton_salir.dibujar()
        boton_salir.cambiar_color(pygame.mouse.get_pos())
        
        
        
        pygame.display.flip()

def puntuaciones(pantalla):
    while True:
        fondo =  pygame.image.load("fondo_espacio.jpg")
        fondo = pygame.transform.scale(fondo,(1080,720))
        pantalla.blit(fondo, fondo.get_rect())

        conexion = sqlite3.connect('bd_btf.db')
        cursor = conexion.cursor()

        cursor = conexion.execute("SELECT nombre, score FROM puntuaciones ORDER BY score DESC LIMIT 10")
        resultados = cursor.fetchall()

        font_puntuaciones = pygame.font.SysFont("arial", 80)

        mejores_score = font_puntuaciones.render("Los 10 mejores estan aqui", True , colores.WHITESMOKE)

        pantalla.blit(mejores_score, (60, 10))

        fuente = pygame.font.Font(None, 36)
        y = 170
        posicion_juego = 1

        for nombre, puntacion in resultados:
            texto = fuente.render(f"{posicion_juego}. {nombre} - {puntacion}", True, colores.WHITE)
            pantalla.blit(texto, (50, y))
            y += 50
            posicion_juego += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE:
                main_menu(pantalla)

        pygame.display.flip()
        

def perdiste(score):
    pygame.init()
    
    pygame.display.set_caption("G.O")
    
    alto_ventana = 720
    ancho_ventana = 1080
    pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
    
    fondo = pygame.image.load("game_over1.jpg")
    fondo = pygame.transform.scale(fondo,(1080,720))
    
    tiempo = pygame.time.Clock()
    manager = pygame_gui.UIManager((ancho_ventana,alto_ventana))
    
    input = pygame_gui.elements.UITextEntryLine(relative_rect= pygame.Rect((300,475),(456,50)),manager = manager,
                                                                                    object_id="#mani_text_entry")
    input_position = pygame.Rect(300,475,456,50)
    
    input.set_text("introduce tu nombre")
    
    flag_correr = True
    while flag_correr:
        ui_tiempo_actualizar = tiempo.tick(60)/1000
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                flag_correr = False
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = pygame.mouse.get_pos()
                if posicion_mouse[0] in range(input_position.left,input_position.right) and posicion_mouse[1] in range(input_position.top,input_position.bottom):
                    input.set_text("")
            
            if evento.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and evento.ui_object_id == "#mani_text_entry":
                crear_tabla_puntuaciones()
                modificar_tabla_puntuaciones(input.get_text(),score)
                puntuaciones(pantalla)
                
            manager.process_events(evento)
            
        manager.update(ui_tiempo_actualizar)
        
        
        pantalla.blit(fondo, (0, 0))
        
        manager.draw_ui(pantalla)
        
        pygame.display.flip()



def jugar():
    alto_ventana = 720
    ancho_ventana = 1080
    pygame.init()
    pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("nvt")
    reloj = pygame.time.Clock()
    fondo = pygame.image.load("fondo.png")
    nave = Nave_pj()
    lista_enemigos = []
    score = 0
    tiempo_pasado = 0
    
    

    flag_correr = True
    while flag_correr:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                flag_correr = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x = nave.rect_torreta.x + 7
                y = nave.rect_torreta.y
                nave.disparar(x, y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and nave.rectangulo.x < 976:
            nave.rectangulo.x = nave.rectangulo.x + 4
        if keys[pygame.K_a] and nave.rectangulo.x > 0:
            nave.rectangulo.x = nave.rectangulo.x - 4

        pantalla.blit(fondo, (0, 0))
        nave.dibujar(pantalla)

        tiempo_pasado += reloj.tick(60) / 1000

        if tiempo_pasado > 1 and len(lista_enemigos) < 5:
            nueva_nave_enemiga = Enemigo()
            lista_enemigos.append(nueva_nave_enemiga)
            tiempo_pasado = 0

        if len(lista_enemigos) > 0:
            for enemigos in lista_enemigos:
                enemigos.dibujar(pantalla)
                enemigos.ataque(enemigos.rectangulo.x, enemigos.rectangulo.y)
                enemigos.movimineto()
                if len(enemigos.lista_disparos) > 0:
                    for proyectil in enemigos.lista_disparos:
                        proyectil.trayectoria()
                        proyectil.dibujar(pantalla)

                        if proyectil.rectangulo_proyectil.colliderect(nave.hitbox_horizontal)or  proyectil.rectangulo_proyectil.colliderect(nave.hitbox_vertical) :
                            nave.vida -= 1
                            if nave.vida == 0:
                                perdiste(score)
                            enemigos.lista_disparos.remove(proyectil)

                        if proyectil.rectangulo_proyectil.y > 720:
                            enemigos.lista_disparos.remove(proyectil)


        if len(nave.listaDisparos) > 0:
            for proyectil in nave.listaDisparos:
                proyectil.trayectoria()
                proyectil.dibujar(pantalla)
                for enemigo in lista_enemigos:
                    if proyectil.rectangulo_proyectil.colliderect(enemigo.rectangulo):
                        enemigo.sonido_explosion.play()
                        nave.listaDisparos.remove(proyectil)
                        lista_enemigos.remove(enemigo)
                        score += 100
                        break

                if proyectil.rectangulo_proyectil.y < 0:
                    nave.listaDisparos.remove(proyectil)

        fuente = pygame.font.Font(None, 36)
        texto_score = fuente.render("Score: " + str(score), True, (255, 255, 255))
        pantalla.blit(texto_score, (10, 10))
        

        pygame.display.flip()
