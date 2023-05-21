import copy

class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")

    def clonar(self):
        return copy.deepcopy(self)


def main():
    carro_original = Carro("Ford", "Mustang", "Vermelho")
    carro_original.exibir_informacoes()

    carro_clone = carro_original.clonar()
    carro_clone.exibir_informacoes()

    carro_clone.cor = "Azul"
    carro_clone.exibir_informacoes()


if __name__ == '__main__':
    main()