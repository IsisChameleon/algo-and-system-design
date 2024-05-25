from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SUPABASE_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Domain : Joke entity
class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# API : Endpoints
# curl -X POST -H "Content-Type: application/json" -d '{"joke": "Why don't scientists trust atoms? Because they make up everything.", "author": "Unknown"}' http://localhost:5000/joke
# curl http://localhost:5000/joke

@app.route('/jokes', methods=['POST'])
def create_joke():
    data = request.get_json()
    joke = Joke(joke=data['joke'], author=data['author'])
    db.session.add(joke)
    db.session.commit()
    return jsonify({'message': 'Joke created successfully'}), 201

@app.route('/jokes/random', methods=['GET'])
def get_random_joke():
    random_joke = db.session.query(Joke).order_by(func.random()).first()
    if random_joke:
        return jsonify({'joke': random_joke.joke, 'author': random_joke.author})
    else:
        return jsonify({'message': 'No jokes found in the database'}), 404

if __name__ == '__main__':
    app.run(debug=True)

# to run the flask app: cd /workspaces/algoexpert/flask_api_skeleton; export FLASK_APP=app.py; flask run
