
# Importar e inicializar Pygame.
import pygame
pygame.init()

# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode((800, 600))
# Poner el título de la ventana.
pygame.display.set_caption("Mi Juego")

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((0, 0, 255))
# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 
salir = False
# Loop principal (game loop) del juego. 
while not salir:

   # Timer que controla el frame rate.
   clock.tick(60)

   # Procesar los eventos que llegan a la aplicación.
   for event in pygame.event.get():
        
       # Si se cierra la ventana se sale del programa.
       if event.type == pygame.QUIT:
           salir = True

       # Si se pulsa la tecla [Esc] se sale del programa.
       if event.type == pygame.KEYUP:
           if event.key == pygame.K_ESCAPE:
               salir = True

   # Actualizar la pantalla.
   
   screen.blit(imgBackground, (0, 0))
   pygame.draw.circle(screen, (0,255,0), [10, 10], 5, 0)
   pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
   pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()