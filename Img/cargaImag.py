import os
import pygame



pygame.init()
tamVentana = (400,400)
tamPant = (tamVentana)
pantalla = pygame.display.set_mode(tamPant)
reloj = pygame.time.Clock()
# Carga de imagenes a una lista de python
imgs = []
imgs.append(pygame.image.load((r'pygame\img\uno.png')))
imgs.append(pygame.image.load((r'pygame\img\dos.png')))
imgs.append(pygame.image.load((r'pygame\img\tres.png')))
imgs.append(pygame.image.load((r'pygame\img\cuatro.png')))
imgs.append(pygame.image.load((r'pygame\img\reverso.png')))

posX = 20
posY = 20
print(imgs)
imgScale = pygame.transform.scale(imgs[0],[30,50])
pxMov = 5
while True:
    pygame.Surface.fill(pantalla,(255,255,255),None)
    
    '''for img in imgs:
        imgRender = pygame.transform.scale(img,[30,50])
        pantalla.blit(imgRender,[posX,10])
        pantalla.blit(img,[posX + 30, 100])
        posX += 40
        posY += 50'''
    pantalla.blit(imgScale,[posX,posY])
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print("Tecla presionada: ",event.type, "Tecla: ",event.key)
            if event.key == pygame.K_s:
                print("Tecla 's/S' apretada",pygame.K_a)
                posY += pxMov
            if event.key == pygame.K_w:
                print("Tecla 'w/W' apretada",pygame.K_q)
                posY -= pxMov
            if event.key == pygame.K_a:
                print("Tecla 'a/A' apretada",pygame.K_q)
                posX -= pxMov
            if event.key == pygame.K_d:
                print("Tecla 'd/D' apretada",pygame.K_q)
                posX += pxMov
    btnIzq, btnMed, btnDer = pygame.mouse.get_pressed()
    if btnIzq:
        posX += pxMov
        posY += pxMov
        print(btnIzq,btnMed,btnDer)
    elif btnMed:
        posX += 10
        print(btnIzq,btnMed,btnDer)
    elif btnDer:
        posY += 10
        print(btnIzq,btnMed,btnDer)
    pygame.display.update()
    reloj.tick(60)