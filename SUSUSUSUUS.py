# INTEGRANTES

# MARTÍN ARRIGO 21.513.208-0
# PATRICIO CUEVAS 21.369.031-0
# MARCOS GUICHAQUELÉN 21.476.012-6
# VÍCTOR GAMBOA 21.343.249-4
# ÁLVARO BURGOS 21.577.347-7

#IMPORTAR MÓDULOS

import pygame, random, sys
ancho=500
alto=500

#FUNCIONES
#FUNCIÓN GENERAR BANANAS

def Generar_Objetos(Mapa):
    x=0
    y=0
    aparicion_banana=0
    banana=0
    aparicion_barrera=0
    barrera=0
    for c in Mapa:
        for i in c:
            if i == 0:
                x+=1
            if i == 1:
                if (random.randint(1,2)==1 ) and banana!=50:
                    aparicion_banana+=1
                    if aparicion_banana%2==1:
                        (Mapa[y])[x]=3
                        banana=banana+1
                        x+=1
                    else:
                        x+=1
                else:
                    if (random.randint(1,2)==1) and barrera!=15:
                        aparicion_barrera+=1
                        if aparicion_barrera%2==1:
                            (Mapa[y])[x]=4
                            barrera=barrera+1
                            x+=1
                        else:
                            x+=1
                    else:
                        x+=1
            elif i == 2:
                if random.randint(1,2)==1 and banana!=50:
                    aparicion_banana+=1
                    if aparicion_banana%2==1:
                        (Mapa[y])[x]=3
                        banana+=1
                        x+=1
                    else:
                        x+=1
                else:
                    x+=1
        x=0
        y+=1
    return Mapa

#FUNCIÓN GENERAR MAPA

def GenerarMapa(mapa,ventana_0,Sprite_muro,Sprite_suelo,Sprite_banana,Sprite_obstaculo):
    x=0
    y=0
    for i in mapa:
        for j in i:
            if j == 0:
                ventana_0.blit(Sprite_muro,(x,y))
                x+=25
            if j == 1 or j==2:
                ventana_0.blit(Sprite_suelo,(x,y))
                x+=25
            if j == 3:
                ventana_0.blit(Sprite_banana,(x,y))
                x+=25
            if j ==4:
                ventana_0.blit(Sprite_obstaculo,(x,y))
                x+=25
        y+=25
        x=0
    
#FUNCIÓN COLISIONES

def ColisionesMapa(mapa,ventana_2,Sprite_muros):
    muros = []
    x = 0
    y = 0
    for muro in mapa:
        for ladrillo in muro:
            if ladrillo == 0:
                muros.append(ventana_2.blit((Sprite_muros),(x,y)))
            x += 25
        x = 0
        y += 25
    return muros

#FUNCIÓN GENERAR BOTS ALEATORIAMENTE

def SpawnBots(ventana_1,sprite):

    x_1=random.choice(range(0,475,25)) 
    y_1=random.choice(range(0,475,25))

    ventana_1.blit(sprite,(x_1,y_1))
    return x_1, y_1

#FUNCIÓN MOVIMIENTO BOTS ALEATORIO

def MovBots(x_0 , y_0, mapa):
    Bot=random.randint(0,4)

    if Bot==0 and x_0!=0 and (mapa[(y_0//25)])[(x_0//25)-1]!=0 and (mapa[(y_0//25)])[(x_0//25)-1]!=4:
        return x_0-25,y_0,mapa

    if Bot==1 and x_0!=475 and (mapa[(y_0//25)])[(x_0//25)+1]!=0 and (mapa[(y_0//25)])[(x_0//25)+1]!=4:
        return x_0+25, y_0,mapa

    if Bot==2 and y_0!=0 and (mapa[(y_0//25)-1])[x_0//25]!=0 and (mapa[(y_0//25)-1])[x_0//25]!=4:
        return x_0,y_0-25,mapa

    if Bot == 3 and y_0!=475 and (mapa[(y_0//25)+1])[x_0//25]!=0 and (mapa[(y_0//25)+1])[x_0//25]!=4:
        return x_0,y_0+25,mapa

    else:
        return x_0,y_0,mapa   

#FUNCIÓN PRINCIPAL

def main():

    #IMPORTAR TABLERO

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

    #INICIAR PYGAME
    #DEFINIR VENTANA
    #DEFINIR X e Y INICIAL DEL JUGADOR
    #CARGAR IMÁGENES

    pygame.init()
    ventana= pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("LA COSA")#Titulo
    ventana.fill((240, 24, 162))

    xCuadradito= 400
    yCuadradito=200

    Sprite_1=pygame.transform.scale((pygame.image.load("player.png").convert()),(25,25))
    Sprite_2=pygame.transform.scale((pygame.image.load("brick.png").convert()),(25,25))#Pared
    Sprite_3=pygame.transform.scale((pygame.image.load("Suelo.png").convert()),(25,25))#Suelo
    Sprite_4=pygame.transform.scale((pygame.image.load("banana_suelo.png").convert()),(25,25))#banana
    Sprite_5=pygame.transform.scale((pygame.image.load("Obstaculo-suelo.png").convert()),(25,25))#Obstucalo

    #LLAMAR FUNCIONES PARA GENERAR EL TABLERO Y JUGADORES

    tablero=Generar_Objetos(tablero)
    GenerarMapa(tablero, ventana,Sprite_2,Sprite_3,Sprite_4,Sprite_5)
    ventana.blit(Sprite_1,(xCuadradito,yCuadradito))
    xEnemigo,yEnemigo=SpawnBots(ventana,Sprite_1)
    xTrip_0,yTrip_0=SpawnBots(ventana,Sprite_1)
    xTrip_1,yTrip_1=SpawnBots(ventana,Sprite_1)

    #ACTUALIZAR VENTANA

    pygame.display.flip()

    #ESTABLECER FPS, VARIABLE TRUE Y CONTADOR INICIAL

    reloj=pygame.time.Clock()
    corriendo=True
    cont=0
    while corriendo:

        #ESTABLECER FPS

        reloj.tick(120) 

        #ACTUALIZAR POSICIÓN DE CADA OBJETO

        GenerarMapa(tablero, ventana,Sprite_2,Sprite_3,Sprite_4,Sprite_5)
        ventana.blit((Sprite_1),(xCuadradito,yCuadradito))
        ventana.blit((Sprite_1),(xEnemigo,yEnemigo))
        ventana.blit((Sprite_1),(xTrip_0,yTrip_0))
        ventana.blit((Sprite_1),(xTrip_1,yTrip_1))

        #AUMENTAR EL CONTADOR

        cont+=1

        #CUANDO EL CONTADOR VALGA 20, LOS BOTS SE MOVERÁN ALEATORIAMENTE

        if cont==10:
            cont=0
            xEnemigo,yEnemigo,tablero=(MovBots(xEnemigo,yEnemigo,tablero))
            xTrip_1,yTrip_1,tablero=(MovBots(xTrip_1,yTrip_1,tablero))
            xTrip_0,yTrip_0,tablero=(MovBots(xTrip_0,yTrip_0,tablero))

        for event in pygame.event.get():

            #CERRAR VENTANA

            if (event.type == pygame.QUIT):
                corriendo=False

            #MOVIMIENTO DEL JUGADOR

            if event.type == pygame.KEYDOWN:
                tecla_P = pygame.key.name(event.key)
                if tecla_P == "w" and yCuadradito!=0 and (tablero[(yCuadradito//25)-1])[xCuadradito//25]!=0 and (tablero[(yCuadradito//25)-1])[xCuadradito//25]!=4 and (tablero[(yCuadradito//25)-1])[xCuadradito//25]!=5 :
                    yCuadradito -=25

                if tecla_P == "a" and xCuadradito!=0 and (tablero[yCuadradito//25])[((xCuadradito//25)-1)]!=0 and (tablero[yCuadradito//25])[((xCuadradito//25)-1)]!=4 and (tablero[yCuadradito//25])[((xCuadradito//25)-1)]!=5:
                   xCuadradito -=25

                if tecla_P == "s" and yCuadradito!=475 and (tablero[(yCuadradito//25)+1])[xCuadradito//25]!=0 and (tablero[(yCuadradito//25)+1])[xCuadradito//25]!=4 and (tablero[yCuadradito//25])[((xCuadradito//25)-1)]!=5:
                    yCuadradito +=25

                if tecla_P == "d" and xCuadradito!=475 and (tablero[yCuadradito//25])[(xCuadradito//25)+1]!=0 and (tablero[yCuadradito//25])[(xCuadradito//25)+1]!=4 and (tablero[yCuadradito//25])[(xCuadradito//25)+1]!=5:
                   xCuadradito +=25

        #ACTUALIZAR VENTANA

        pygame.display.flip()

    #CERRAR LA VENTANA

    sys.exit()
main()
