import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key,esTilde):

    ###################################
    # Permite ingresar tildes
    if esTilde: # → esTilde verifica si el usario presiona la tilde + una vocal
        if key==K_a:
            return ("á")
        elif key==K_e:
            return ("é")
        elif key==K_i:
            return ("í")
        elif key==K_o:
            return ("ó")
        elif key==K_u:
            return ("ú")

    ###################################


    ###################################
    # Permite ingresar consonantes y vocales

    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == 59:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    ###################################

    elif key == K_KP_MINUS:# → ingresa "menos"
        return("-")
    elif key == K_SPACE:# → "ingresa "espacio"
       return(" ")


    ###################################
    # Permite ingresar numeros con las teclas de escrituras

    elif key == K_0:
        return("0")
    elif key == K_1:
        return("1")
    elif key == K_2:
        return("2")
    elif key == K_3:
        return("3")
    elif key == K_4:
        return("4")
    elif key == K_5:
        return("5")
    elif key == K_6:
        return("6")
    elif key == K_7:
        return("7")
    elif key == K_8:
        return("8")
    elif key == K_9:
        return("9")
    ###################################



    ###################################
   # Permite ingresar numeros con el teclado numérico

    elif key == K_KP0:
        return("0")
    elif key == K_KP1:
        return("1")
    elif key == K_KP2:
        return("2")
    elif key == K_KP3:
        return("3")
    elif key == K_KP4:
        return("4")
    elif key == K_KP5:
        return("5")
    elif key == K_KP6:
        return("6")
    elif key == K_KP7:
        return("7")
    elif key == K_KP8:
        return("8")
    elif key == K_KP9:
        return("9")
    ###################################

    else:
        return("")





def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra el nombre
    screen.blit(defaultFont.render(ayuda, 1, COLOR_PELI), (ANCHO//2-len(ayuda)*TAMANNO_LETRA//4,(TAMANNO_LETRA)))

    #muestra las 2 lineas
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_LETRAS), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*2))
    screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*4))


