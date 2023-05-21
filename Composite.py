from abc import ABC, abstractmethod

class Produto(ABC):
    @abstractmethod
    def get_preco(self):
        pass

    def adicionar_produto(self, produto):
        pass

    def remover_produto(self, produto):
        pass

class Item(Produto):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.preco

class Pacote(Produto):
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def get_preco(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco()
        return total

def main():
    item1 = Item("Camiseta", 29.99)
    item2 = Item("Calça", 49.99)
    item3 = Item("Meia", 9.99)
    item4 = Item("Jogo", 59.99)
    item5 = Item("Tenis", 199.99)

    pacote = Pacote("Pacote de Roupas")
    pacote.adicionar_produto(item1)
    pacote.adicionar_produto(item2)
    pacote.adicionar_produto(item3)
    pacote.adicionar_produto(item4)
    pacote.adicionar_produto(item5)
    print(f"Preço total do pacote: R$ {pacote.get_preco()}")
    pacote.remover_produto(item3)

    print(f"Preço total do pacote: R$ {pacote.get_preco()}")

if __name__ == '__main__':
    main()
