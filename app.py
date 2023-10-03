from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/pdfs.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return app.config['SQLALCHEMY_DATABASE_URI']


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)