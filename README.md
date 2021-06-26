# Homeautomation System with Raspberry Pi
![SmartHome](https://github.com/joselinosantosti/automacao-raspberrypi/blob/master/smarthome.png)

# Desenvolvido com Python, Flask e Firebase permite o controle remoto através da rede local e Internet.

## Itens necessários
* Raspberry Pi3
* Relé
* Jumpers
* Sensores (Se quiser melhorar ainda mais)

## Etapas
## 1. Conexõs físicas
Faça um esquema no Fritzing para definir qual pino será usado em qual dispositivo. Como na figura:

-O pino com conexão vermelha é o VCC, alimenta com 5V
-O pino com conexão preta é o GND(terra)
-O pino com conexão amarela é o 13 (GPIO), o que vamos conectar ao dispositivo a ser controlado
-O relé contém módulos, estamos utilizando o primeiro, atenção no processo das conexões para não danificar o Rasp nem apresentar mal funcionamento 
Para saber mais sobre as GPIO consulte ![Raspberry Pi GPIO](https://www.w3schools.com/nodejs/nodejs_raspberrypi_gpio_intro.asp)

## 2. Instalação do sistema operacional e pacotes necessários
Se o seu Rasp for novo acompanhe o seguinte manual para instalação e configuração:
![Instalação do SO](https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp)

## 3. Instalando os pacotes necessários
Abra o terminal e digite
sudo su (digite a senha)
apt-get update && apt-get upgrade
pip install flask jinja2

## 4. Estruturando o projeto  Flask
Crie uma pasta com o nome smarthome ou outro.
Crie as subpastas
-static
-templates
-controllers
-models
Crie o arquivo app.py e adicione o código que está no projeto.


## 4. Módulo para controlar dispositivos localmente
...

## 5. Módulo para conexão com Firebase e controle via Internet
...
