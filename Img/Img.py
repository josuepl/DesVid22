
import pygame, sys, time
#variables de inicilización
maxX = 800
maxY = 600
fondo = (0, 0, 0)
inicio = True
iniX = 100
iniY = 100
pygame.init()
imgScale=[80,80]
pantalla = pygame.display.set_mode((maxX, maxY))
imagen = pygame.image.load("./Img/mario2.png")
img2 = pygame.transform.scale(imagen,imgScale)
mario2 = pygame.image.load("./Img/mario.png")
m2 = pygame.transform.scale(mario2,imgScale)
print(img2)
regreso = True

while True:
    x = 2
    cont = 0
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    print(iniX," - " ,iniY," - ", cont)
    if inicio:
        pantalla.blit(img2, (100, 100))
        inicio = False
    else:
        if (iniX <= 760) & (iniY <= 540) & (regreso):
            iniX+=x
            iniY+=x
            pantalla.fill(fondo)
            pantalla.blit(img2, (iniX, iniY))
        else:
            regreso = False
            if(iniX <= 100) & (iniY<=100):
                regreso = True
            iniX-=x
            iniY-=x
            pantalla.fill(fondo)
            pantalla.blit(m2, (iniX, iniY))
        cont+=1


    pygame.display.update()
    time.sleep(.02)