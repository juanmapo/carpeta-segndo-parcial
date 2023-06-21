import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de recolección de estrellas")

# Colores
WHITE = (255, 255, 255)

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Clase para representar al personaje
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (window_width // 2, window_height - 50)
    
    def update(self):
        # Obtener la posición del ratón
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
    
    def draw(self):
        window.blit(self.image, self.rect)

# Clase para representar una estrella
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = random.randint(0, window_width - self.rect.width)
            self.rect.y = -self.rect.height
            self.speed = random.randint(1, 5)
    
    def draw(self):
        window.blit(self.image, self.rect)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()

# Crear el personaje y agregarlo al grupo de sprites
player = Player()
all_sprites.add(player)

# Variables de juego
score = 0
game_time = 30  # Tiempo en segundos
start_time = pygame.time.get_ticks()

# Bucle principal del juego
running = True
while running:
    # Controlar el tiempo transcurrido
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar el personaje
    all_sprites.update()
    
    # Generar estrellas aleatoriamente
    if random.randint(0, 100) < 3:
        star = Star()
        all_sprites.add(star)
        stars.add(star)
    
    # Colisión entre el personaje y las estrellas
    hits = pygame.sprite.spritecollide(player, stars, True)
    for star in hits:
        score += 1
    
    # Limpiar la pantalla
    window.fill((0, 0, 0))
    
    # Dibujar todos los sprites
    all_sprites.draw(window)
    
    # Mostrar la puntuación
    font = pygame.font.Font(None, 36)
    text = font.render("Puntuación: " + str(score), True, WHITE)
    window.blit(text, (10, 10))
    
    # Mostrar el tiempo restante
    remaining_time = max(game_time - elapsed_time, 0)
    text = font.render("Tiempo: " + str(int(remaining_time)), True, WHITE)
    window.blit(text, (window_width - 150, 10))
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Comprobar si se acabó el tiempo
    if elapsed_time >= game_time:
        running = False

    # Controlar la velocidad de actualización
    clock.tick(60)

# Mostrar la puntuación final
final_font = pygame.font.Font(None, 72)
final_text = final_font.render("Puntuación final: " + str(score), True, WHITE)
window.blit(final_text, (window_width // 2 - final_text.get_width() // 2, window_height // 2 - final_text.get_height() // 2))
pygame.display.flip()

# Esperar unos segundos antes de cerrar la ventana
pygame.time.wait(3000)

# Salir del juego
pygame.quit()
