class Sensor:
    def detectar_movimento(self):
        print("Sensor detectou movimento.")


class SistemaDeAlarme:
    def ativar_alarme(self):
        print("Alarme ativado.")


class AdaptadorSensorParaAlarme(SistemaDeAlarme):
    def __init__(self, sensor):
        self.sensor = sensor

    def ativar_alarme(self):
        self.sensor.detectar_movimento()
        print("Alarme ativado.")


def main():
    sensor = Sensor()
    adaptador = AdaptadorSensorParaAlarme(sensor)

    adaptador.ativar_alarme()


if __name__ == '__main__':
    main()