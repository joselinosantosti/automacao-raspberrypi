import RPi.GPIO as gpio

class Device:
    def __init__(self):

        gpio.setmode(gpio.BOARD)
        
        # Limpar o cache quando retornar mensagem de que esta em uso
        gpio.cleanup

    # Ligar ou desligar
    def acionar(self, pino, acao):
        gpio.setup(pino, gpio.OUT)
        gpio.output(pino, acao)
