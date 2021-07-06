# Homeautomation System - Raspberry Pi 3
![SmartHome](https://github.com/joselinosantosti/automacao-raspberrypi/blob/master/smarthome.png)

# Desenvolvido com Python, Flask e Firebase permite o controle remoto através da rede local e Internet.

## Itens necessários
* Raspberry Pi3
* Relé
* 1 dispositivo para ser controlado (Usei uma lâmpada, mas pode ser qualquer outro)
* Jumpers
* Sensores (Se quiser melhorar ainda mais)

## Etapas
## 1. Conexõs físicas
Faça um esquema no Fritzing para definir qual pino será usado em qual dispositivo. Como na figura:<br>
![Esquema](https://github.com/joselinosantosti/homeautomation-raspberrypi/blob/master/esquema.png)
-O pino com conexão vermelha é o VCC, alimenta com 5V<br>
-O pino com conexão preta é o GND(terra)<br>
-O pino com conexão amarela é o 13 (GPIO), o que vamos conectar ao dispositivo a ser controlado<br>
-O relé contém módulos, estamos utilizando o primeiro, atenção no processo das conexões para não danificar o Rasp nem ocorrer mal funcionamento.<br>
Para saber mais sobre as GPIO consulte ![Raspberry Pi GPIO](https://www.w3schools.com/nodejs/nodejs_raspberrypi_gpio_intro.asp)

## 2. Instalação do sistema operacional
Se o seu Rasp for novo acompanhe o seguinte manual para instalação e configuração:
[Instalação do SO](https://www.w3schools.com/nodejs/nodejs_raspberrypi.asp)
Ou acompanhe o minicurso do ![Curso em vídeo](https://www.youtube.com/watch?v=iBMXYA5rva8&list=PLHz_AreHm4dnGZ_nudmN4rvyLk2fHFRzy&index=11)

## 3. Criando virtualenv e instalando os pacotes necessários
Abra o terminal e digite
sudo su (digite a senha)
apt-get update && apt-get upgrade
apt install virtualenv

## Crie o virtualenv
virtualenv venv

## Instale os pacotes
pip install flask jinja2

## 4. Estruturando o projeto  Flask
Crie uma pasta com o nome smarthome ou outro.
Crie as subpastas
-static<br>
-templates<br>
-controllers<br>
-models<br>
Crie o arquivo app.py e adicione o código que está no projeto.

## 5. Módulo para controlar dispositivos localmente
...

## 6. Módulo para conexão com Firebase e controle via Internet
...
