
from configuracion import *
import random
import math
import unicodedata
import pygame
from pygame.locals import *

def musica():
        lista=[]
        pygame.mixer.music.load("Sonidos/musica.wav")#Cargamos musica de fondo
        pygame.mixer.music.play() #Iniciamos la musica de fondo
        pygame.mixer.music.set_volume(0.02) #Volumen de la musica de fondo
        acierto=pygame.mixer.Sound("Sonidos/acierto.wav")#Cargamos los sonidos
        fallo=pygame.mixer.Sound("Sonidos/error.wav")
        aplausos=pygame.mixer.Sound("Sonidos/aplausos.wav")
        risas=pygame.mixer.Sound("Sonidos/risas.wav")
        fin=pygame.mixer.Sound("Sonidos/fin.wav")
        #Volumen de los sonidos
        acierto.set_volume(0.1)
        fallo.set_volume(0.1)
        aplausos.set_volume(0.1)
        risas.set_volume(0.1)
        fin.set_volume(0.1)
        #Agregamos los sonidos a una lista
        lista.append(acierto)#0
        lista.append(fallo)#1
        lista.append(aplausos)#2
        lista.append(risas)#3
        lista.append(fin)#4
        return (lista)


def imagen():

        lista=[]
        #Cargamos las imagenes
        fondo=pygame.image.load("Imagenes/fondo.jpg")
        callejeros=pygame.image.load("Imagenes/callejeros.jpg")
        mana=pygame.image.load("Imagenes/mana.jpg")
        yatra=pygame.image.load("Imagenes/yatra.jpg")
        charlygarcia=pygame.image.load("Imagenes/charlygarcia.jpg")
        kapanga=pygame.image.load("Imagenes/kapanga.jpg")
        leongieco=pygame.image.load("Imagenes/leongieco.jpg")
        losredondos=pygame.image.load("Imagenes/losredondos.jpg")
        namuncura=pygame.image.load("Imagenes/namuncura.jpg")
        payaso=pygame.image.load("Imagenes/payaso.jpg")
        shakira=pygame.image.load("Imagenes/shakira.jpg")
        #Agregamos las imagenes a una lista
        lista.append(fondo)#0
        lista.append(yatra)#1
        lista.append(kapanga)#2
        lista.append(callejeros)#3
        lista.append(charlygarcia)#4
        lista.append(payaso)#5
        lista.append(leongieco)#6
        lista.append(losredondos)#7
        lista.append(mana)#8
        lista.append(shakira)#9
        lista.append(namuncura)#10
        return (lista)


def artista(lista):
    num=0
    if lista[0]=="yatra":  #Para identificar al artista, le asiganamos un número
        num=1              #Que es el mismo número que su imagen en la lista
    elif lista[0]=="kapanga":
        num=2
    elif lista[0]=="callejeros":
        num=3
    elif lista[0]=="charly garcia":
        num=4
    elif lista[0]=="piñon fijo":
        num=5
    elif lista[0]=="leon gieco":
        num=6
    elif lista[0]=="los redondos":
        num=7
    elif lista[0]=="mana":
        num=8
    elif lista[0]=="shakira":
        num=9
    else:
        num=10 #namuncurá los primitos del morales
    return num




def cargar_artistaYcancion(cancion,artistaYcancion):

    #Inicio de la carga de Artista y Cancion

    palabra=""

    for elemento in cancion[0][:-1].lower()+";":# → Cargo la 1ra linea del archivo cancion, en la lista "artistaYcancion"

        if elemento!=";": # → Separa las opciones del usuario sin los ;

                palabra=palabra+ elemento

        else:
            artistaYcancion.append(palabra)
            palabra=""


    #Fin de la carga...


def cargar_letra (cancion,letra):

    #Inicio de la carga de la letra completa del archivo "cancion"

    for i in range (1, len(cancion)): # →  recorre desde  1 hasta el ultimo indice del archivo

        if len(cancion[i])!=0 and len(cancion[i]) <=51: #se queda solo con los oraciones de cierta longitud

            letra.append(cancion[i][:-1]) # cargo linea x linea la letra de la cancion, sin los \n



def lectura(archivo, letra, artistaYcancion):

    cancion=archivo.readlines()


    cargar_artistaYcancion(cancion,artistaYcancion)
    cargar_letra(cancion,letra)


    print(artistaYcancion)





def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente


    lineasX=random.randint(0,len(letra)-2)# devuelve un numero entre 0 y los elemenos de la lista
                                          #sin contar el ultimo elemento

    linea1=letra[lineasX]
    linea2=letra[lineasX+1]

    return (linea1,linea2) # → devuevle la linea 1 y su siguiente



def puntos(n):

    return 2**n
    #devuelveel puntaje, segun seguidilla




def esCorrecta(palabraUsuario, artistaYCancion, correctas):


    for elemento in artistaYCancion:
        if elemento==palabraUsuario:

            return puntos(correctas)

    return (-1)
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla








