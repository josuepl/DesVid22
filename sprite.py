import pygame
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Objeto(pygame.sprite.Sprite):
    def __init__(self, color, tam) -> None:
        super().__init__()
        self.image = pygame.Surface(tam)
        self.image.fill(color)
        # Se agrega imagen
        #self.image = pygame.image.load("obstaculo.png").convert()
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() # Se asigna el espacio X,Y 
                                          #donde se muestra en pantalla
    pass

class Player(pygame.sprite.Sprite):
    def __init__(self, color, tam) -> None:
        super().__init__()
        self.image = pygame.Surface(tam)
        self.image.fill(color)
        # Se agrega imagen
        #self.image = pygame.image.load("obstaculo.png").convert()
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def mov(self):
        mousePos = pygame.mouse.get_pos()
        player.rect.x = mousePos[0]
        player.rect.y = mousePos[1]
        pass
    pass

pygame.init()
tamPant = [800, 600]
pantalla = pygame.display.set_mode(tamPant)
fin = False
clock =  pygame.time.Clock()
fondo = pygame.image.load("fondo.png").convert()
#carga de objetos
objList = pygame.sprite.Group()
allSpriteList = pygame.sprite.Group()

for i in range(50):
    color = (random.randrange(0,255,1),random.randrange(0,255,1),random.randrange(0,255,1))
    tam =[20,20]
    obj = Objeto(color,tam)
    obj.rect.x = random.randrange(tamPant[0])
    obj.rect.y = random.randrange(tamPant[1])
    objList.add(obj)
    allSpriteList.add(obj)

#Jugador
player = Player(WHITE,[30,30])
allSpriteList.add(player)
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
    #Mover el jugador a la posicion del puntero

    
    #Colisiones
    hitObjList = pygame.sprite.spritecollide(player, objList,True)
    mousePos = pygame.mouse.get_pos()
    player.mov()
    tamP = 30
    pantalla.blit(fondo,[0,0])
    allSpriteList.draw(pantalla)
    posCircle = (mousePos[0]+tamP/2, mousePos[1] + tamP/2)
    pygame.draw.circle(pantalla,BLACK,posCircle,tamP/2,1)
    pygame.display.flip()
    clock.tick(60)    
    pass
pygame.quit()