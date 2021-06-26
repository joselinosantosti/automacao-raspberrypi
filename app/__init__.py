# Importar
from flask import Flask
from flask_script import Manager, Server

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
#manager.add_command("runserver", Server(host="10.0.0.102", port=5000))
manager.add_command("runserver", Server(port=6000))

from app.models import Device
from app.controllers import routes