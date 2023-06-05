import os
from flask import Flask

class Config:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'secret'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dlyaproekta.diplom@gmail.com'
    MAIL_DEFAULT_SENDER = 'dlyaproekta.diplom@gmail.com'
    MAIL_PASSWORD = 'nynfdinwztnsnhuc'


app = Flask(__name__)
app.config.from_object(Config())

