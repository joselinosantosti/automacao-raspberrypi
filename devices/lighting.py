# Importa lib de data e  hora
import time

# Importa biblioteca da GPIO
import RPi.GPIO as gpio

# Define as variaveis de hora e minuto (Apenas para  o modo auto)
horas = time.strftime("%H")
minutos = time.strftime("%M")
hora_atual = time.strftime("%H:%M")

# Define o pino 7 no modo BOARD
pino = 13
gpio.setmode(gpio.BOARD)

# Define o pino como saida
gpio.setup(pino, gpio.OUT)

# Limpar o cache quando retornar mensagem de que esta em uso
gpio.cleanup

# Funcao com condicao para ligar ou desligar
def acionar(manual=False, acao=True):
    '''
    Funcao com condicao para ligar ou desligar dispositivo
    :param manual: determina se a acao sera manual (True) ou automatica (False)
    '''
    if manual == True:
        if acao == True:
            #status = gpio.input(pino)
            #gpio.output(pino, not status)
            gpio.output(pino, 0)
        else:
            gpio.output(pino, 1)
    else:
        # Mantem ligado das 7 da manha as 23h30
        '''if int(horas) == 23 or int(horas) < 7 and manual==False:
        gpio.output(pino, 1)
        print('Desligado')
        elif manula == True:
        gpio.output(pino, acao)
        print('Ligado')
        ''' 	
acionar()

