import pygame
#CREAR BOTTON
class Botton:
    #CREAR EL DISÑEO DEL BOTON
    def __init__(self, x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        #CLICK CANTIDAD DER VECES
        self.cliked = False
    #LO MUETRA EN LA PANTALLA
    def draw(self, surfece):
        #ACCION DE BOTONES INDEPENDIENTES
        accion = False
        #MUESTRA EL RAOToN
        pos = pygame.mouse.get_pos()
        #print(pos)
        #VER SI ESTA SOBRE EL BOTNON
        if self.rect.collidepoint(pos):
            #verdadero si se pultsa click derecho
            if pygame.mouse.get_pressed()[0] == 1 and self.cliked == False:
                self.cliked = True
                accion = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.cliked =  False
        surfece.blit(self.image, (self.rect.x,self.rect.y))
        return accion