# INTEGRANTES

# MARTÍN ARRIGO 21.513.208-0
# PATRICIO CUEVAS 21.369.031-0
# MARCOS GUICHAQUELÉN 21.476.012-6
# VÍCTOR GAMBOA 21.343.249-4
# ÁLVARO BURGOS 21.577.347-7

#Modulos
import pygame, random, sys
ancho=500
alto=500
###   Temporal ###
color_Trip=(173, 173, 173)
color_Cosa=(255,255,255)
### Temporal ###
def SpawnBots(v_1,color):#Generacion de los tripulantes aleatorias
    ### Temporal ###
    x_1=random.choice([0,475]) 
    y_1=random.choice([0,475])
    ### Temporal ###
    pygame.draw.rect(v_1,color, pygame.Rect(x_1, y_1, 25, 25))
    return x_1, y_1
def MovBots(x_0 , y_0):#Movimiento para la cosa y los tripulantes
    Bot=0
    Bot=random.randint(0,4)
    if Bot==0 and x_0!=0:
        return x_0-25,y_0
    if Bot==1 and x_0!=475:
        return x_0+25, y_0
    if Bot==2 and y_0!=0:
        return x_0,y_0-25
    if Bot == 3 and y_0!=475:
        return x_0,y_0+25
    else:
        return x_0,y_0   
def main():
    pygame.init()
    ventana= pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Eres la cosa")#Titulo
    ventana.fill((240, 24, 162))
    xCuadradito= 400
    yCuadradito=200
    pygame.draw.rect(ventana, (0,0,0), pygame.Rect( xCuadradito,yCuadradito, 25,25))
    xEnemigo,yEnemigo=SpawnBots(ventana,color_Cosa)
    xTrip_0,yTrip_0=SpawnBots(ventana,color_Trip)
    xTrip_1,yTrip_1=SpawnBots(ventana,color_Trip)
    pygame.display.flip()
    reloj=pygame.time.Clock()
    corriendo=True
    cont=0
    while corriendo:
        reloj.tick(120)
        ventana.fill((240, 24, 162)) #Rellenar fondo
        #Actualizacion de posicion
        pygame.draw.rect(ventana, (0,0,0), pygame.Rect( xCuadradito,yCuadradito, 25,25))
        pygame.draw.rect(ventana, (color_Cosa), pygame.Rect( xEnemigo,yEnemigo, 25,25))
        pygame.draw.rect(ventana, (color_Trip), pygame.Rect( xTrip_0,yTrip_0, 25,25))
        pygame.draw.rect(ventana, (color_Trip), pygame.Rect( xTrip_1,yTrip_1, 25,25))
        cont+=1
        if cont==20:
            cont=0
            xEnemigo,yEnemigo=(MovBots(xEnemigo,yEnemigo))
            xTrip_1,yTrip_1=(MovBots(xTrip_1,yTrip_1))
            xTrip_0,yTrip_0=(MovBots(xTrip_0,yTrip_0))
        for event in pygame.event.get(): #Cerrar ventana
            if (event.type == pygame.QUIT):
                corriendo=False
            if event.type == pygame.KEYDOWN: #Movimiento del Jugador
                tecla_P = pygame.key.name(event.key)
                if tecla_P == "w" and yCuadradito!=0:
                    yCuadradito -=25
                if tecla_P == "a" and xCuadradito!=0:
                   xCuadradito -=25
                if tecla_P == "s" and yCuadradito!=475:
                    yCuadradito +=25
                if tecla_P == "d" and xCuadradito!=475:
                   xCuadradito +=25
        pygame.display.flip()
    sys.exit() #Cerrar
main()
