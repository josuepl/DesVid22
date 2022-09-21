
import math
import random
import pygame


class Figura:
    def __init__(self, x, y, tam, vel, acel) -> None:
        self.x = x
        self.y = y
        self.tam = tam
        self.vel = vel
        self.pos = [self.x, self.y]
        self.acel = acel
        self.color = [random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)]
        self.dirX = self.dirY = 1
        pass

    def movfig(self):
        self.vel = self.vel*self.acel
        self.y = self.y + self.dirY*self.vel
        self.x = self.x + self.dirX*self.vel

        if self.x >= 800:
            self.dirX = -1
        if self.x <= 0:
            self.dirX = 1
        if self.y >= 200:
            self.dirY = -1
        if self.y <= 0:
            self.dirY = 1
        pass

    def detecCols(self, figura, pant):
        distX = self.pos[0] - figura.pos[0]
        distY = self.pos[1] - figura.pos[1]
        distT = math.sqrt(math.pow(distX, 2)+math.pow(distY, 2))
        tamT = self.tam + figura.tam + .005
        #print("Dist:", distT, "tamT:",tamT)
        if distT < tamT: # detecta colisión
            if distT != 0:
                #print("Se detecto una colision ",tamT, "dist:",distT)
                self.color =[random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)]
                self.pos = [10,10]
        #bordes inferiores
        if (self.pos[0] - self.tam) < 0:
            self.pos[0] = 10
        if (self.pos[1] - self.tam) < 0:
            self.pos[1] = 10
        #bordes superiores
        if (self.pos[0] + self.tam) > pant[0]:
            self.pos[0] = pant[0] - self.tam
        if (self.pos[1] + self.tam) > pant[1]:
            self.pos[1] = pant[1] - self.tam

        pass
    pass

class Juego:
    FONDO = [255, 255, 255]
    COLOR = [0, 0 ,0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    listaObj = []
    def __init__(self, tamPant) -> None:
        self.tamPant = tamPant
        self.screen = pygame.display.set_mode(tamPant)
        self.clock = pygame.time.Clock() 
        pass
    
    def agregaObjetos(self) -> None:
        tamObj = 10
        obj = Figura(11, 11, tamObj, 1, 1)
        self.listaObj.append(obj)
        alto = self.tamPant[1]
        ancho = self.tamPant[0]
        totalP = 10
        for i in range (1, totalP):
            x = random.randrange(30, ancho - tamObj)
            y = random.randrange(30, alto - tamObj)
            print("X:", x, "Y:", y)
            obj = Figura(x, y, tamObj, 1, 1)
            self.listaObj.append(obj)
        pass


    def interaccion(self) ->None:
        self.Activa = True
        while self.Activa:
            self.clock.tick(60)
            obj = self.listaObj[0]
            for obj2 in self.listaObj:
                #print("OBJ1:",obj,"OBJ2: ",obj2)
                if(obj != obj2):
                    #print("Distinto !!!")
                    obj.detecCols(obj2, self.tamPant)
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Activa = False
                #Evento de Teclado
                if event.type == pygame.KEYDOWN:
                    print("POS",obj.pos)
                    if event.key == pygame.K_ESCAPE:
                        self.Activa = False
                    if event.key == pygame.K_w:
                        self.listaObj[0].pos[1]-=  self.listaObj[0].dirY*self.listaObj[0].vel         
                    if event.key == pygame.K_s:
                        self.listaObj[0].pos[1]+= self.listaObj[0].dirY*self.listaObj[0].vel
                        
            #Evento de Teclado
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.listaObj[0].pos[1]-=  self.listaObj[0].dirY*self.listaObj[0].vel                       
            if keys[pygame.K_s]:
                self.listaObj[0].pos[1]+= self.listaObj[0].dirY*self.listaObj[0].vel
            if keys[pygame.K_a]:
                self.listaObj[0].pos[0]-=  self.listaObj[0].dirX*self.listaObj[0].vel                       
            if keys[pygame.K_d]:
                self.listaObj[0].pos[0]+= self.listaObj[0].dirX*self.listaObj[0].vel
            #Evento de Raton
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                btn = pygame.mouse.get_pressed()
                print("Posicion de raton: ", pos, "Boton: ", btn)
            #Redibujo en pantalla    
            self.screen.fill(self.FONDO)
            for obj in self.listaObj:
                pygame.draw.circle(self.screen, obj.color , obj.pos, obj.tam)
                pass   
            pygame.display.flip()
        pygame.quit()
        pass
    pass

def main():
    print("MENU")
    tamPant = [500, 200]
    game = Juego(tamPant)
    game.agregaObjetos()
    game.interaccion()
    pass

if __name__ == "__main__":
    main()
    pass
