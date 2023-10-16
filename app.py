from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, DateTime, text
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/policies.db'
db = SQLAlchemy(app)

class Policies(db.Model):
    _id = db.Column(Integer, primary_key=True)
    policy_id = db.Column(String(255))
    branch = db.Column(String(255))
    policy_type = db.Column(String(255))
    policy_name = db.Column(Text)
    policy_text = db.Column(Text)
    upload_time = db.Column(DateTime, server_default=text('(CURRENT_TIMESTAMP)'))


@app.route('/')
def index():
    return app.config['SQLALCHEMY_DATABASE_URI']


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)