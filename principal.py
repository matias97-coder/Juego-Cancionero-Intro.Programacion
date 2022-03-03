#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *



#Funcion principal
def main():


        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        #Iniciamos pygame y mixer
        pygame.init()
        pygame.mixer.init()

        #CARGAR MUSICA Y SONIDOS
        #La función "musica" retorna una lista con los sonidos
        sonido=musica()

        #CARGAR IMAGENES
        #La función imagen retorna una lista con las imágenes
        imagenes=imagen()

        #Preparar la ventana
        pygame.display.set_caption("Cancionero...")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        #definimos funciones


        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial
        artistaYcancion=[]
        puntos = 0
        palabraUsuario = ""
        letra=[]
        correctas=0
        elegidos= []
        masDeUnaVuelta = False
        esTilde=False
        malaracha=0


        #cargo una imagen de fondo


        #elige una cancion de todas las disponibles
        azar=random.randrange(1,N+1)
        elegidos.append(azar) #la agrega a la lista de los ya elegidos
        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8') # abre el archivo elegido con unicode.


        #lectura del archivo y filtrado de caracteres especiales, la primer linea es el artista y cancion
        lectura(archivo, letra, artistaYcancion)

        #elige una linea al azar y su siguiente
        lista=seleccion(letra)

##        print(lista)

        ayuda = "Cancionero"
        dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
        for elemento in letra:
                print (elemento)
        while segundos > fps/1000:


        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:

                    letraApretada = dameLetraApretada(e.key,esTilde)

                    if e.key == 39: # pregunto si el usurio ingreso una tilde
                        esTilde=True
                    else:
                        esTilde=False

                    palabraUsuario += letraApretada

                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, artistaYcancion, correctas)
                        puntos+=sumar

                        if sumar>0:


                            correctas=correctas+1
                            malaracha=0
                            if correctas>=3:
                                sonido[2].play()
                            else:
                                sonido[0].play()
                        else:

                            correctas=0
                            malaracha=malaracha+1

                            if malaracha>=3:
                                sonido[3].play()
                            else:
                                sonido[1].play()
                            ##Cuando el jugador falla, en el juego se muestra la imagen del artista
                            autor=artista(artistaYcancion)     #Función "artista" devuelve un entero
                            if autor==1:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[1],[300,230])  #Mostramos la imagen en pantalla
                                    tiempo=tiempo+1
                                    pygame.display.flip()  #Refrescamos la pantalla
                            if autor==2:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[2],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==3:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[3],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==4:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[4],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==5:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[5],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==6:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[6],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==7:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[7],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==8:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[8],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==9:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[9],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()
                            if autor==10:
                                tiempo=0
                                while tiempo<500:
                                    screen.blit(imagenes[10],[300,230])
                                    tiempo=tiempo+1
                                    pygame.display.flip()

                        if len(elegidos)==N:
                                elegidos=[]
                                masDeUnaVuelta = True

                        azar=random.randrange(1,N+1)
                        while(azar in elegidos):
                            azar=random.randrange(1,N+1)

                        elegidos.append(azar)

                        if masDeUnaVuelta == True:
                            ayuda = artistaYcancion[0]


                        archivo= open(".\\letras\\"+str(azar)+".txt","r", encoding='utf-8')
                        palabraUsuario = ""
                        #lectura del archivo y filtrado de caracteres especiales
                        artistaYcancion=[]
                        letra = []
                        lectura(archivo, letra, artistaYcancion)

                        #elige una linea al azar y su siguiente
                        lista=seleccion(letra)


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior

            screen.blit(imagenes[0], [0,0])  #Cargamos la imagen de fondo


            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
            pygame.display.flip()
        pygame.mixer.music.pause()
        sonido[4].play()
        fuente = pygame.font.Font(None,50)
        textofinal = fuente.render("¡Gracias por jugar!",0,(255,255,255))
        alumnos = fuente.render("Nicolás Lavia | Matías Ortigoza",0,(234, 203, 77))
        screen.blit(textofinal,(300,300))
        screen.blit(alumnos,(10,500))
        pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return


        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
