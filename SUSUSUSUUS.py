#MARTÍN ARRIGO 21.513.208-0
#PATRICIO CUEVAS 21.369.031-0
#MARCOS GUICHAQUELÉN 21.476.012-8
#VÍCTOR GAMBOA 21.343.249-4
#ÁLVARO BURGOS 21.577.347-7
import pygame
import sys
import random
#Constantes
ANCHO = 500
ALTO = 500
#Función principal
def main():
    pygame.init()
    #Definir ventana y coordenadas del jugador
    ventana=pygame.display.set_mode((ANCHO, ALTO))
    tablero= [
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
    [0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
    [1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
    [1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
    [0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
    [0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
    [0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
    [0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
    [0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
    [2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
    [2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
    [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
    ]
    xMorcos=0
    yMorcos=25
    pygame.display.set_caption("Las maravillosas desventuras de Morcos")
    #Darle FPS al juego
    reloj=pygame.time.Clock()
    pygame.display.flip()
    corre=True
    #Movimientos en general, del jugador, enemigo
    while corre:
        reloj.tick(60)
        ventana.fill((192, 162, 250))
        #Dibujar al jugador
        pygame.draw.rect(ventana,(153, 131, 8), pygame.Rect(xMorcos,yMorcos,25,25))
        #Dibujar al enemigo
        xEnemigo=400
        yEnemigo=400
        pygame.draw.rect(ventana,(255, 0, 0), pygame.Rect(xEnemigo,yEnemigo,25,25))
        x=random.randint(0,4)
        if x==0 and xEnemigo!=0:
            xEnemigo -=25
        if x==1 and xEnemigo!=450:
            xEnemigo +=25
        if x==2 and yEnemigo!=0:
            yEnemigo -=25
        if x==3 and yEnemigo!=450:
            yEnemigo +=25
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                corre=False
            #Movimientos del jugador
            if event.type == pygame.KEYDOWN:
                tecla_P=pygame.key.name(event.key)
                if tecla_P== "w":
                    yMorcos -=25
                if tecla_P== "a":
                    xMorcos -=25
                if tecla_P== "s":
                    yMorcos +=25
                if tecla_P== "d":
                    xMorcos +=25
        pygame.display.flip()
    sys.exit()
main()
