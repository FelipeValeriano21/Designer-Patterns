class Pizza:
    def __init__(self):
        self.tipo = ""
        self.tamanho = ""
        self.ingredientes = []

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def get_pizza(self):
        return f"Tipo: {self.tipo}, Tamanho: {self.tamanho}, Ingredientes: {', '.join(self.ingredientes)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_tipo(self, tipo):
        self.pizza.set_tipo(tipo)

    def set_tamanho(self, tamanho):
        self.pizza.set_tamanho(tamanho)

    def add_ingrediente(self, ingrediente):
        self.pizza.add_ingrediente(ingrediente)

    def get_pizza(self):
        return self.pizza


def main():
    builder = PizzaBuilder()
    builder.set_tipo("Margherita")
    builder.set_tamanho("Média")
    builder.add_ingrediente("Queijo")
    builder.add_ingrediente("Molho de tomate")
    builder.add_ingrediente("Manjericão")
    pizza = builder.get_pizza()
    
    builder1 = PizzaBuilder()
    builder1.set_tipo("Toscana")
    builder1.set_tamanho("Pequena")
    builder1.add_ingrediente("Calabresa")
    builder1.add_ingrediente("Molho de tomate")
    builder1.add_ingrediente("Queijo")
    pizza1 = builder1.get_pizza()


    print(pizza.get_pizza())
    print(pizza1.get_pizza())



if __name__ == '__main__':
    main()