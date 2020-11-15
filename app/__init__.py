# Importar
from flask import Flask
from flask_script import Manager, Server

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
manager.add_command("runserver", Server(host="10.0.0.102", port=5000))

from app.devices import lighting
from app.controllers import default