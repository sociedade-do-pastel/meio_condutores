from flask import Flask

app = Flask(__name__) # construtor padrão do flask

from app import routes
