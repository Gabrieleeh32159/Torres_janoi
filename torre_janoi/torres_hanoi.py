import pygame
import sys
from disco import Disco


class Inicio:
    def __init__(self):
        pygame.init()

        self.reloj = pygame.time.Clock()

        self.automatic = False

        self.negro = (0, 0, 0)
        self.rojo = (255, 0, 0)
        self.verde = (0, 255, 0)
        self.gris = (200, 200, 200)
        self.blanco = (255, 255, 255)

        self.color_barra = (225, 195, 120)

        self.fuente = pygame.font.SysFont("impact", 45)

        self.ancho = 1200
        self.alto = 800
        self.dimensiones = (self.ancho, self.alto)

        #self.play_again_button = pygame.Rect((300, ), ())

        self.ancho_barra = 20

        self.barra1_x = self.ancho / 4 - self.ancho_barra / 2 - 100
        self.barra2_x = self.ancho / 2 - self.ancho_barra / 2
        self.barra3_x = self.ancho * 3/ 4 - self.ancho_barra / 2 + 100

        self.screen = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption("Torres de Hanoi")
        self.pantalla_rect = self.screen.get_rect()

    def mostrar_torre(self, torre, numero):
        dicc = {1: self.barra1_x, 2: self.barra2_x, 3: self.barra3_x}
        pos_y = 580
        for i in range(1, len(torre)):
            disco = torre[i]
            x = dicc[numero] + 10 - (disco.ancho / 2)
            pygame.draw.rect(self.screen, disco.color, [x, pos_y, disco.ancho, disco.alto], 0)
            pos_y -= disco.alto

    def mostrar_escenario(self, torre1, torre2, torre3):
        pasar = False
        while not pasar:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return False
                    elif evento.key == pygame.K_RETURN:
                        self.automatic = True

            self.screen.fill(self.gris)

            pygame.draw.rect(self.screen, self.color_barra, [0, self.alto / 2 + 200, self.ancho, self.alto / 2 - 200], 0)
            pygame.draw.rect(self.screen, self.color_barra, [self.barra1_x, 200, self.ancho_barra, 400])
            pygame.draw.rect(self.screen, self.color_barra, [self.barra2_x, 200, self.ancho_barra, 400])
            pygame.draw.rect(self.screen, self.color_barra, [self.barra3_x, 200, self.ancho_barra, 400])

            self.mostrar_torre(torre1, torre1[0])
            self.mostrar_torre(torre2, torre2[0])
            self.mostrar_torre(torre3, torre3[0])

            pygame.display.flip()
            self.reloj.tick(20)
            if self.automatic:
                pasar = True

    def start(self):
        continuar = False
        altura = ""
        error = False
        while not continuar:
            enter = False
            nombre_text = self.fuente.render("Ingrese la altura de la torre: " + altura, True, self.negro)
            error_msg = self.fuente.render("La altura ingresada no es un entero, intenta de nuevo. ", True, self.rojo)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif evento.key == pygame.K_RETURN:
                        enter = True
                    elif evento.key == pygame.K_BACKSPACE:
                        altura = altura[:-1]
                    else:
                        altura += evento.unicode
            self.screen.fill(self.blanco)

            self.screen.blit(nombre_text, (300, 330))
            if enter:
                try:
                    altura = int(altura)
                    continuar = True
                except:
                    error = True

            if error:
                self.screen.blit(error_msg, (100, 430))
            pygame.display.flip()

        letras = [Disco(self, chr(x)) for x in range(ord('A'), ord('A') + altura)]
        torre1 = [1] + letras
        torre2 = [2]
        torre3 = [3]

        self.mostrar_escenario(torre1, torre2, torre3)
        self.pasa_torre(altura, torre1, torre3, torre2)

        input()
        '''
        pregunta = self.fuente.render("Desea ingresar una nueva altura?", True, self.negro)
        si_txt = self.fuente.render("SI", True, self.verde)
        no_txt = self.fuente.render("NO", True, self.rojo)

        si_button = si_txt.get_rect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if si_button.collidepoint(pygame.mouse.get_pos()):
                        return True

            self.screen.fill(self.blanco)

            self.screen.blit(pregunta, (270, 330))
            self.screen.blit(si_txt, (400, 400))
            self.screen.blit(no_txt, (490, 400))
            
        

            pygame.display.flip()
        '''

    def pasa_disco(self, inicio, fin, medio):
        disco = inicio[-1]
        inicio.pop()
        fin.append(disco)
        self.mostrar_escenario(inicio, medio, fin)

    def pasa_torre(self, alto, inicio, fin, intermedio):
        if alto >= 1:
            self.pasa_torre(alto - 1, inicio, intermedio, fin)
            self.pasa_disco(inicio, fin, intermedio)
            self.pasa_torre(alto - 1, intermedio, fin, inicio)


#play_again = True
#while play_again:
game = Inicio()
game.start()
