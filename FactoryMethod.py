from abc import ABC, abstractmethod

# Classe abstrata que representa um animal
class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

# Classe concreta para representar um cachorro
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

# Classe concreta para representar um gato
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Classe concreta para representar um pássaro
class Passaro(Animal):
    def fazer_som(self):
        return "Piu Piu!"
    
class Peixe(Animal):
    def fazer_som(self):
        return "Blu!"

# Classe fábrica abstrata
class FabricaAnimais(ABC):
    @abstractmethod
    def criar_animal(self):
        pass



# Classe fábrica concreta para criar um cachorro
class FabricaCachorro(FabricaAnimais):
    def criar_animal(self):
        return Cachorro()

# Classe fábrica concreta para criar um gato
class FabricaGato(FabricaAnimais):
    def criar_animal(self):
        return Gato()

# Classe fábrica concreta para criar um pássaro
class FabricaPassaro(FabricaAnimais):
    def criar_animal(self):
        return Passaro()

class FabricaPeixe(FabricaAnimais):
    def criar_animal(self):
        return Peixe()
# Função principal
def main():
    fabrica_cachorro = FabricaCachorro()
    fabrica_gato = FabricaGato()
    fabrica_passaro = FabricaPassaro()
    fabrica_peixe = FabricaPeixe()

    cachorro = fabrica_cachorro.criar_animal()
    gato = fabrica_gato.criar_animal()
    passaro = fabrica_passaro.criar_animal()
    peixe = fabrica_peixe.criar_animal()

    print(cachorro.fazer_som())
    print(gato.fazer_som())
    print(passaro.fazer_som())
    print(peixe.fazer_som())

if __name__ == '__main__':
    main()