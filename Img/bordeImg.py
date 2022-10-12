
import pygame
class Elemento:
    def __init__(self, posX, posY, tamX, tamY,color) -> None:
        self.imgPath = r'img\uno.png'
        self.img = pygame.transform.scale(pygame.image.load(self.imgPath),(40,55)) 
        self.posXY = (posX, posY)
        self.color = color
        self.margen = (posX-1,posY-1,tamX +2,tamY+2)
        self.tamXY = (tamX,tamY)
        pass
    def actualizaMargen(self):
        self.margen = (self.posXY[0] - 1,self.posXY[1] - 1, self.tamXY[0] + 2,self.tamXY[1]+2)
    pass


class Juego():
    def __init__(self, anchoV, altoV) -> None:
        self.ventana = (anchoV, altoV)
        self.fondo = (0, 0, 0)
        self.rojo = (255, 0 , 0)
        self.azul = (0, 0, 255)
        self.objs = []
        self.reloj = pygame.time.Clock()
    pass

    def initGame(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode(self.ventana)
        elem = Elemento(10,10,40,55,None)
        self.objs.append(elem)
        pass

    def startGame(self):
        while True:
            #Carga de imagenes
            '''
            Carga de Escenerario
            Carga de Objetos de interacción
            Carga de Personajes
            '''
            pygame.Surface.fill(self.pantalla,(255,255,255),None)
            pygame.draw.rect(self.pantalla,self.rojo,self.objs[0].margen,0)
            pygame.Surface.blit(self.pantalla,self.objs[0].img, self.objs[0].posXY)
            

            '''
            Carga de audios y sonidos
            '''

            '''
            Interaccion -  Eventos
            Teclado
            Raton

            '''

            for event in pygame.event.get():
                #print(event.type)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    print("Tecla presionada: ",event.type, "Tecla: ",event.key)
                    if event.key == pygame.K_s:
                        print("Tecla 's/S' apretada",pygame.K_s)
                        print(self.objs[0].posXY)
                        auxX =self.objs[0].posXY[0]
                        auxY = self.objs[0].posXY[1]
                        auxY += 2
                        self.objs[0].posXY = (auxX,auxY)
                        #posY += pxMov
                    if event.key == pygame.K_w:
                        print("Tecla 'w/W' apretada",pygame.K_w)
                        print(self.objs[0].posXY)
                        auxX =self.objs[0].posXY[0]
                        auxY = self.objs[0].posXY[1]
                        auxY -= 2
                        self.objs[0].posXY = (auxX,auxY)
                        #posY -= pxMov
                    if event.key == pygame.K_a:
                        print("Tecla 'a/A' apretada",pygame.K_a)
                        print(self.objs[0].posXY)
                        auxX =self.objs[0].posXY[0]
                        auxY = self.objs[0].posXY[1]
                        auxX -= 2
                        self.objs[0].posXY = (auxX,auxY)
                        #posX -= pxMov
                    if event.key == pygame.K_d:
                        print("Tecla 'd/D' apretada",pygame.K_d)
                        print(self.objs[0].posXY)
                        auxX =self.objs[0].posXY[0]
                        auxY = self.objs[0].posXY[1]
                        auxX += 2
                        self.objs[0].posXY = (auxX,auxY)
                        #posX += pxMov
                btnIzq, btnMed, btnDer = pygame.mouse.get_pressed()
                if btnIzq:
                    #posX += pxMov
                    #posY += pxMov
                    print(btnIzq,btnMed,btnDer)
                elif btnMed:
                    #posX += 10
                    print(btnIzq,btnMed,btnDer)
                elif btnDer:
                    #posY += 10
                    print(btnIzq,btnMed,btnDer)
                pygame.display.update()
                self.reloj.tick(60)
                pass
            '''
            Actualizar elementos
            '''
            self.objs[0].actualizaMargen()
        pass

def main():
    juego = Juego(400,400)
    juego.initGame()
    juego.startGame()
    pass

if __name__ == "__main__":
    main()