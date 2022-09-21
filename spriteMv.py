"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
  
Vídeo explicativo: http://youtu.be/qbEEcQXw8aw
"""
  
import pygame
import random
  
# Definimos algunos colores
 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
  
 
class Bloque(pygame.sprite.Sprite):
    """
    Esta clase representa El objeto general de el juego.        
    Deriva de la clase "Sprite" en Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Le pasa el color al bloque, 
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__() 
  
        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
        # Extraemos el objeto rectángulo que posee las dimensiones de la imagen.
        # Estableciendo los valores para rect.x and rect.y actualizamos la posición de este objeto.
        self.rect = self.image.get_rect()
         
    def reset_pos(self):
        """ Restablecemos la posición en la parte alta de la pantalla, en una ubicación aleatoria x.
        Si hubiera una colisión, sería llamada por update() o por el bucle principal.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(700-20)        
 
    def update(self):
        """ Llamada para cada fotograma. """
 
        # Desplaza el bloque un píxel hacia abajo.
        self.rect.y += 1
         
        # Si el bloque estuviera muy abajo, lo restablecemos a la parte superior de la pantalla.
        if self.rect.y > 410:
            self.reset_pos()
 
class Protagonista(Bloque):
    """ La clase protagonista deriva de Bloque, pero sobrescribe su funcionalidad de 'update' 
    por una nueva función de desplazamiento que moverá el bloque con el ratón. """
    def update(self):
        # Obtiene la posición actual del ratón. La devuelve en forma de 
        # una lista de dos números.
        pos = pygame.mouse.get_pos()
          
        # Extraemos x e y de la lista, tal como si extrajéramos letras de una cadena de texto (string).
        # Coloca al objeto protagonista en la posición del ratón.
        self.rect.x = pos[0]
        self.rect.y = pos[1]        
         
# Iniciamos Pygame
pygame.init()
  
# Establecemos el largo y alto de la pantalla
largo_pantalla = 700
alto_pantalla = 400
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
  
# Esta es una lista de 'sprites.' Cada bloque en el programa es 
# añadido a esta lista. La lista bes gestionada por la clase llamada  'Group.'
bloque_lista = pygame.sprite.Group()
  
# Esta es una lista de cada sprite, así como de los bloques y del protagonista.rojo
listade_todoslos_sprites= pygame.sprite.Group()
  
for i in range(50):
    # Esto representa un bloque
    bloque = Bloque(NEGRO, 20, 15)
  
    # Establece una ubicación aleatoria para el bloque
    bloque.rect.x = random.randrange(largo_pantalla)
    bloque.rect.y = random.randrange(alto_pantalla)
      
    # Añade el bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
      
      
  
# Crea un bloque protagonista de color rojo
protagonista = Protagonista(ROJO, 20, 15)
listade_todoslos_sprites.add(protagonista)
  
# Iteramos hasta que el usuario haga click sobre el botón de salir.
hecho = False
  
# Lo usamos para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
  
puntuacion = 0
  
# -------- Bucle Principal del Programa -----------
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
  
    #Limpiamos la pantalla
    pantalla.fill(BLANCO)
     
    # Llamamos al método update() para cada sprite en la lista
    listade_todoslos_sprites.update()
      
    # Observamos si el bloque protagonista ha colisionado con algo
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)  
      
    # Comprobamos la lista de colisiones
    for bloque in lista_impactos_bloques:
        puntuacion += 1
        print( puntuacion )
         
        # Restablecemos al bloque, en la parte alta de la pantalla, para que vuelva caer.
        bloque.reset_pos() 
          
    # Dibujamos todos los sprites
    listade_todoslos_sprites.draw(pantalla)
      
    # Limitamos a 20 fotogramas por segundo
    reloj.tick(20)
  
    # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado.
    pygame.display.flip()
  
pygame.quit()