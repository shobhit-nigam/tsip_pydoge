from flask import Flask

app = Flask(__name__)

from tsipapp import routes
from tsipapp import three

