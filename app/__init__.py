__version__ = "0.1"
from flask import Flask

app = Flask('app')
app.config['SECRET_KEY'] = 'secreto'

app.debug = True

@app.route('/')
def main():
    return "  "