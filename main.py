import pygame
import sys
import random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)
GREEN = (0 ,255, 0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")
#CONTROLAR LOS FRAMES
clock = pygame.time.Clock()
def play():
    print("SIIII")
#Se crea el objeto personaje

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #CARGA LA IMAGEN DEL PERSONAJE
        self.image = pygame.image.load("assets/cuadernoF1.png").convert()
        #REMOVER FONDO DE LA IMAGEN
        self.image.set_colorkey(BLACK)
        #CUADRO DE LA IMAGEN
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.vida = 100
    def update(self):
        self.speed_x = 0
        #MOVIMIENTOS CON EL TECLADO
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        #SI LLEGA AL TAMAÑO DE ANCHURA LA VELOCIDAD ES IGUAL A 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
#SE CREA LOS ENEMIGOS
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 10)

class Meteor1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteorGrey_med1.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 10)

def vidas(surface,x ,y, hp):
    Blarga = 150
    Bancho = 15
    lleno = (hp/100) * Blarga
    borde = pygame.Rect(x, y, Blarga, Bancho)
    lleno = pygame.Rect(x, y, lleno, Bancho)
    pygame.draw.rect(surface, GREEN, lleno)
    pygame.draw.rect(surface, WHITE, borde, 2)
    corazones = pygame.image.load("assets/cuadernoF1.png").convert()
    screen.blit(pygame.transform.scale(corazones, (25, 25)),(620,2))


# FONDO
fondo =  pygame.image.load("assets/Fondo1.png").convert()
#se alamacena el jugador
all_sprites = pygame.sprite.Group()
meteor_list = pygame.sprite.Group()

meteor_list1 = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(10):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_list.add(meteor)

for i in range(10):
    meteor1 = Meteor1()
    all_sprites.add(meteor1)
    meteor_list1.add(meteor1)

running = True
aux = 1
Fuente = pygame.font.SysFont("consola",20)
while running:
    clock.tick(60)
    screen.fill(BLACK)
    Tiempo = int(pygame.time.get_ticks()/1000)
    if aux == Tiempo:
        aux += 1
        print(Tiempo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    #COLISIONES
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    #Si choca con un meteoro 4 veces el juego acaba
    for i in hits:
        player.vida -= 25
        print("HIT")
        if player.vida <= 0:
            running = False
    contador = Fuente.render("MARCADOR :"+str(Tiempo), 0, (120, 70, 0))
    vidas(screen, 650, 5, player.vida)
    screen.blit(contador, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
