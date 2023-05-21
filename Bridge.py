class FormaGeometrica:
    def __init__(self, implementador):
        self.implementador = implementador

    def desenhar(self):
        pass


class ImplementadorDesenho:
    def desenhar_forma(self):
        pass


class ImplementadorDesenhoRed:
    def desenhar_forma(self):
        print("Na cor vermelha.")


class ImplementadorDesenhoBlue:
    def desenhar_forma(self):
        print("Na cor.")


class Quadrado(FormaGeometrica):
    def desenhar(self):
        print("Desenhando um quadrado.")
        self.implementador.desenhar_forma()


class Circulo(FormaGeometrica):
    def desenhar(self):
        print("Desenhando um círculo.")
        self.implementador.desenhar_forma()


def main():
    quadrado_red = Quadrado(ImplementadorDesenhoRed())
    quadrado_red.desenhar()

    circulo_blue = Circulo(ImplementadorDesenhoBlue())
    circulo_blue.desenhar()


if __name__ == '__main__':
    main()