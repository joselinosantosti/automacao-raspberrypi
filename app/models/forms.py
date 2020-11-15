from flask_wtf import FlaskForm
from wtforms import BooleanField

class ControlForm(FlaskForm):
    lamp = BooleanField("lamp")