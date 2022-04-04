
class Disco:
    def __init__(self, game, letra):
        numero = ord(letra) - ord('A') + 1
        colores = {1: (0, 0, 80), 2: (0, 0, 160),
                   3: (0, 0, 240), 4: (80, 80, 0),
                   5: (160, 160, 0), 6: (240, 240, 0),
                   7: (80, 0, 0), 8: (160, 0, 0),
                   9: (240, 0, 0)}
        self.color = colores[numero]
        self.screen = game.screen
        self.ancho = 30 * (10 - numero)
        self.alto = 20
