
import pygame
import sys
import button
import random

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego")
black = (0, 0, 0)
fondo = pygame.image.load("assets/Fondo_Menu.png").convert_alpha()
#BOTON CREADO START
startimg = pygame.image.load("assets/Start_Menu.png").convert_alpha()
startimg = button.Botton(300, 290, startimg, 0.5)
#Boton De Info
infoimg = pygame.image.load("assets/Info_Menu.png").convert_alpha()
infoimg = button.Botton(300, 375, infoimg, 0.5)
#BOTON CREADO EXIT
exitimg = pygame.image.load("assets/Exit_Menu.png").convert_alpha()
exitimg = button.Botton(300, 458, exitimg, 0.5)
def info():
    black = (0, 0, 0)
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("INFO")
    info = pygame.image.load("assets/intro.png").convert_alpha()
    run = True
    while run:
        ventana.blit(info, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            press = pygame.key.get_pressed()
            if press[pygame.K_SPACE]:
                run = False
            if event.type == pygame.QUIT:
                run = False

def play():
    ANCHO = 800
    ALTO = 600
    BLACK = (0, 0 , 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    pygame.init()
    pygame.mixer.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego1")
    pygame.mixer.music.load("assets/musica.mp3")
    pygame.mixer.music.play(2)
    #CONTROLAR LOS FRAMES
    clock = pygame.time.Clock()
    #Se crea el objeto personaje
    class Jugador(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            #CARGA LA IMAGEN DEL PERSONAJE
            self.image = pygame.image.load("assets/Personaje.png").convert()
            #REMOVER FONDO DE LA IMAGEN
            self.image.set_colorkey(BLACK)
            #CUADRO DE LA IMAGEN
            self.rect = self.image.get_rect()
            self.rect.centerx = ANCHO // 2
            self.rect.bottom = ALTO - 10
            self.speed_x = 0
            self.vida = 100
            self.puntos = 0
        def update(self):
            self.speed_x = 0
            #MOVIMIENTOS CON EL TECLADO
            mov = pygame.key.get_pressed()
            if mov[pygame.K_LEFT]:
                self.speed_x = -5
            if mov[pygame.K_RIGHT]:
                self.speed_x = 5
            self.rect.x += self.speed_x
                #SI LLEGA AL TAMAÑO DE ANCHURA LA VELOCIDAD ES IGUAL A 0
            if self.rect.right > ANCHO:
                self.rect.right = ALTO
            if self.rect.left < 0:
                self.rect.left = 0
    #SE CREA LOS ENEMIGOS
    class enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = random.choice(lista)
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 10)
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 25:
                self.rect.x = random.randrange(ANCHO - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(3, 8)

    class ingles(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = random.choice(lista1)
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(9, 10)
        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > ALTO + 10 or self.rect.left < -25 or self.rect.right > ANCHO + 25:
                self.rect.x = random.randrange(ANCHO - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(3, 10)
    def vidas(surface, x, y, hp):
        Blarga = 150
        Bancho = 15
        lleno = (hp / 100) * Blarga
        borde = pygame.Rect(x, y, Blarga, Bancho)
        lleno = pygame.Rect(x, y, lleno, Bancho)
        pygame.draw.rect(surface, GREEN, lleno)
        pygame.draw.rect(surface, WHITE, borde, 2)
        corazones = pygame.image.load("assets/CuadernoF1.png").convert()
        ventana.blit(pygame.transform.scale(corazones, (25, 25)), (620, 2))
#ENEMIGOD
    lista = []
    listaimg = ["assets/Palabra_4.png", "assets/Palabra_5.png", "assets/Palabra_6.png"]
    lista1 = []
    listaimg1 = ["assets/Palabra_1.png", "assets/Palabra_2.png", "assets/Palabra_3.png"]
    for j in listaimg:
        lista.append(pygame.image.load(j).convert())
    for j in listaimg1:
        lista1.append(pygame.image.load(j).convert())
    #FONDO
    fondo = pygame.image.load("assets/Fondo_Juego.png").convert()
    gameover = pygame.image.load("assets/Game over.png").convert()
    #se alamacena el jugador
    sprite = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    enemigos1 = pygame.sprite.Group()
    player = Jugador()
    sprite.add(player)
    for i in range(10):
        ene = enemy()
        sprite.add(ene)
        enemigos.add(ene)
        ################## NO COLISIONES ########################
    for i in range(3):
        ene1 = ingles()
        sprite.add(ene1)
        enemigos1.add(ene1)
    ############################################################
    def generaing():
        for i in range(1):
            ene1 = ingles()
            sprite.add(ene1)
            enemigos1.add(ene1)
    def generaenemy():
        for i in range(1):
            ene = enemy()
            sprite.add(ene)
            enemigos.add(ene)
    def sonidos1():
        sonido = pygame.mixer.Sound("assets/si.mp3")
        sonido.play()

    def sonidos2():
         sonido = pygame.mixer.Sound("assets/Golpe.mp3")
         sonido.play()
    run = True
    aux = 1
    Fuente = pygame.font.SysFont("consola",40)
    while run:
        clock.tick(60)
        ventana.fill(BLACK)
        Tiempo = int(pygame.time.get_ticks()/1000)
        if aux == Tiempo:
            aux += 1
            print(Tiempo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        sprite.update()
        #COLISIONES
        hits = pygame.sprite.spritecollide(player, enemigos, True)
        hitsING = pygame.sprite.spritecollide(player, enemigos1, True)
        #Si choca con un meteoro 4 veces el juego acaba
        if hits:
            sonidos2()
            player.vida -= 25
            if player.puntos == 0:
                player.puntos -= 0
            else:
                player.puntos -= 20
            generaenemy()
        if hitsING:
            sonidos1()
            if player.vida == 100:
                player.puntos += 20
            else:
                player.vida += 25
                player.puntos += 20
            generaing()
        print(player.puntos)
        if player.vida <= 0:
            print("F")
            run = False
        contador = Fuente.render("Tiempo :"+str(Tiempo), 0, (0, 0, 0))
        puntuaje = Fuente.render("Marcador :"+str(player.puntos), 0, (0, 0, 0))
        ventana.blit(fondo, (0, 0))
        vidas(pantalla, 650, 5, player.vida)
        ventana.blit(contador, (0, 0))
        ventana.blit(puntuaje, (0, 40))
        sprite.draw(ventana)
        pygame.display.flip()
        ventana.blit(gameover, (0, 0))
#FINALADEL CODIGO DEL JUEGOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
run = True
while run:
    pantalla.blit(fondo, (0, 0))
    for event in pygame.event.get():
        if exitimg.draw(pantalla):
            run = False
        if event.type == pygame.QUIT:
            run = False
        if infoimg.draw(pantalla):
            info()
        if startimg.draw(pantalla):
            play()
        pygame.display.update()
pygame.quit()


