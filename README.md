# controle-leds-php-raspberrypi3
Esse script usa a função shell-exec do php para executar scripts python no Raspberry pi 3

1. Instale todos os softwares necessários
sudo apt-get install php7.0
sudo apt-get install apache2

2. Crie um projeto como o nome que desejar no diretório /var/www/html e adicine os seguintes arquivos
index.php
acende.py
apaga.py

3. Adicione o conteúdo dos arquivos

4. Dê permissão total para a pasta com o seguinte comando no Linux:
chmod 777 -R /var/www/html/led

5. Procure o IP do Raspberry com o comando ifconfig e digite no navegador da seguinte forma:
192.168.1.4/led


