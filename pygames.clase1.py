import pygame

COLOR_VENTANA = (139, 123, 139)
ANCHO_VENTANA = 800
LARGO_VENTANA = 600
RADIO_CIRCULO = 50
posicion_circulo = [250, 250]
posicion_pala = [400, 400]
# Timer
timer_segundos = pygame.USEREVENT  # evento del usuario

pygame.init()
pygame.time.set_timer(timer_segundos, 100)
# Imagen
imagen_pala = pygame.image.load("pala.jpg")
imagen_pala = pygame.transform.scale(imagen_pala, (100, 100))
# Texto
fuente = pygame.font.SysFont("Calibri", 24)
texto = fuente.render("CORRE DE LA PALA", True, (248, 248, 255))
screen = pygame.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pygame.display.set_caption("ejercicio 1")
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        """ if event.type == pygame.MOUSEMOTION:
            posicion_circulo = event.pos """
        """ if event.type == pygame.USEREVENT:
                if event.type == timer_segundos:
                    if posicion_circulo[0] < ANCHO_VENTANA + RADIO_CIRCULO  and posicion_circulo[1] < LARGO_VENTANA + RADIO_CIRCULO:
                        posicion_circulo[0] += 10
                        posicion_circulo[1] += 10
                    else:
                        posicion_circulo[0] = 0
                        posicion_circulo[1] = 0 """
        """ if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posicion_circulo[0] = posicion_circulo[0] + 10
                if event.key == pygame.K_LEFT:
                    posicion_circulo[0] = posicion_circulo[0] - 10
                if event.key == pygame.K_UP:
                    posicion_circulo[1] = posicion_circulo[1] - 10
                if event.key == pygame.K_DOWN:
                    posicion_circulo[1] = posicion_circulo[1] + 10  """
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_pala = event.pos

    """ lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas [pygame.K_RIGHT]:
            posicion_circulo[0] = posicion_circulo[0] + 0.02
        if lista_teclas [pygame.K_LEFT]:
            posicion_circulo[0] = posicion_circulo[0] - 0.02
        if lista_teclas [pygame.K_UP]:
            posicion_circulo[1] = posicion_circulo[1] - 0.02
        if lista_teclas [pygame.K_DOWN]:
                posicion_circulo[1] = posicion_circulo[1] + 0.02  """

    screen.fill(COLOR_VENTANA)
    screen.blit(imagen_pala, posicion_pala)
    screen.blit(texto, [300, 100])
    """ pygame.draw.circle(screen, (255, 165, 0), posicion_circulo,RADIO_CIRCULO) """

    pygame.display.flip()


pygame.quit()

