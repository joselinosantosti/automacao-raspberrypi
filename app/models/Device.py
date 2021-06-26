# Importa lib de data e  hora
import time

# Importa biblioteca da GPIO
import RPi.GPIO as gpio

class Device:
    def __init__(self):
        self.pino = 0

    # Controle manual
    # Define o pino 7 no modo BOARD
    self.pino = 13
    gpio.setmode(gpio.BOARD)

    # Define o pino como saida
    gpio.setup(pino, gpio.OUT)

    # Limpar o cache quando retornar mensagem de que esta em uso
    gpio.cleanup

    # Funcao com condicao para ligar ou desligar
    def acionar(acao=True):
        '''
        Funcao com condicao para ligar ou desligar dispositivo
        :param acao: determina se a acao sera ligar (True) ou desligar (False)
        '''
        if self.acao == True:
            #status = gpio.input(pino)
            #gpio.output(pino, not status)
            gpio.output(pino, 0)
        else:
            gpio.output(pino, 1)


