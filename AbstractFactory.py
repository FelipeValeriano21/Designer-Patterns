from abc import ABC, abstractmethod

# Classe abstrata que representa um botão
class Botao(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# Classe concreta para representar um botão em estilo "light"
class BotaoLight(Botao):
    def renderizar(self):
        return "Renderizando um botão em estilo light."

# Classe concreta para representar um botão em estilo "dark"
class BotaoDark(Botao):
    def renderizar(self):
        return "Renderizando um botão em estilo dark."

# Classe abstrata que representa um campo de texto
class CampoTexto(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# Classe concreta para representar um campo de texto em estilo "light"
class CampoTextoLight(CampoTexto):
    def renderizar(self):
        return "Renderizando um campo de texto em estilo light."

# Classe concreta para representar um campo de texto em estilo "dark"
class CampoTextoDark(CampoTexto):
    def renderizar(self):
        return "Renderizando um campo de texto em estilo dark."

# Classe abstrata da fábrica abstrata
class FabricaComponentes(ABC):
    @abstractmethod
    def criar_botao(self):
        pass
    @abstractmethod
    def criar_campo_texto(self):
        pass

# Classe concreta da fábrica para criar componentes em estilo "light"
class FabricaComponentesLight(FabricaComponentes):
    def criar_botao(self):
        return BotaoLight()
    def criar_campo_texto(self):
        return CampoTextoLight()

# Classe concreta da fábrica para criar componentes em estilo "dark"
class FabricaComponentesDark(FabricaComponentes):
    def criar_botao(self):
        return BotaoDark()
    def criar_campo_texto(self):
        return CampoTextoDark()

# Função principal
def main():
    fabrica_light = FabricaComponentesLight()
    fabrica_dark = FabricaComponentesDark()

    botao_light = fabrica_light.criar_botao()
    campo_texto_light = fabrica_light.criar_campo_texto()

    botao_dark = fabrica_dark.criar_botao()
    campo_texto_dark = fabrica_dark.criar_campo_texto()

    print(botao_light.renderizar())
    print(campo_texto_light.renderizar())
    print(botao_dark.renderizar())
    print(campo_texto_dark.renderizar())

if __name__ == '__main__':
    main()