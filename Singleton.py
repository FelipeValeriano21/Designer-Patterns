class Configuracao:
    _instancia = None

    def __init__(self):
        self.valor_configuracao = ""

    @staticmethod
    def obter_instancia():
        if not Configuracao._instancia:
            Configuracao._instancia = Configuracao()
        return Configuracao._instancia


def main():
    configuracao1 = Configuracao.obter_instancia()
    configuracao1.valor_configuracao = "Configuração 1"

    configuracao2 = Configuracao.obter_instancia()
    print(configuracao2.valor_configuracao)  # Saída: "Configuração 1"

    configuracao3 = Configuracao.obter_instancia()
    print(configuracao3.valor_configuracao)  # Saída: "Configuração 1"



if __name__ == '__main__':
    main()