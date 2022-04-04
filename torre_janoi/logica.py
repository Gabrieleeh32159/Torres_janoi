def pasa_disco(inicio, fin):
    disco = inicio[-1]
    inicio.pop()
    fin.append(disco)
    print("Mueve: ")
    mostrar_torres()


def pasa_torre(alto, inicio, fin, intermedio):
    if alto >= 1:
        pasa_torre(alto-1, inicio, intermedio, fin)
        pasa_disco(inicio, fin)
        pasa_torre(alto-1, intermedio, fin, inicio)


def mostrar_torres():
    print(torre1)
    print(torre2)
    print(torre3)


altura = int(input("Altura de la torre: "))
torre1 = [chr(x) for x in range(ord('A'), ord('A') + altura)]
torre2 = []
torre3 = []
mostrar_torres()
pasa_torre(altura, torre1, torre3, torre2)
