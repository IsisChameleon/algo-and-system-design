import uuid
from flask import Flask, request, jsonify, redirect, abort
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortUrlId = db.Column(db.String(10), unique=True, nullable=False)
    longUrl = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    expiryDate = db.Column(db.DateTime, nullable=True)

def generate_short_id(num_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))

@app.route('/shorten', methods=['POST'])
def create_short_url():
    data = request.json
    long_url = data.get('longUrl')
    if not long_url:
        return jsonify({'error': 'Missing longUrl parameter'}), 400
    
    short_id = str(uuid.uuid4())
    
    new_url = URL(shortUrlId=short_id, longUrl=long_url)
    db.session.add(new_url)
    db.session.commit()

    short_url = request.host_url + short_id
    return jsonify({'shortUrl': short_url})

@app.route('/<shortUrlId>')
def redirect_to_long_url(shortUrlId):
    url_entry = db.session.query(URL).filter_by(shortUrlId=shortUrlId).first()
    if url_entry and (not url_entry.expiryDate or url_entry.expiryDate > datetime.utcnow()):
        return redirect(url_entry.longUrl, code=301)
    else:
        abort(404, description="URL not found or expired")

if __name__ == '__main__':
    db.create_all()  # This line should be used to create the database schema initially
    app.run(debug=True)


"""
What is a 301 Redirect?
A 301 redirect is an HTTP status code that indicates a permanent redirection. 
When a web server responds with a 301 status code, it tells the browser that the resource requested has been permanently moved to a new URL. 
This type of redirect is useful for SEO purposes because search engines update their indexes to reflect the new URL, 
ensuring that link equity is transferred from the old URL to the new one.

3. Methods to Handle Collisions
Collisions occur when the generated short URL is not unique. Here are some methods to handle them:

a. Hash-Based Generation
Use a hashing algorithm (e.g., MD5, SHA-1) to generate a fixed-length string from the long URL.
To avoid collisions, store the hash in the database and check for its existence before using it.
If a collision is detected, append a counter or use a different hashing algorithm.

b. Random String Generation
Generate a random alphanumeric string of fixed length (e.g., 6-8 characters).
Check the database for existing entries with the same short URL.
If a collision is detected, regenerate the string until a unique one is found.

c. Sequential Unique ID
Use a sequential unique ID (e.g., auto-increment integer) and convert it to a different base (e.g., base62) to create a short URL.
This method ensures uniqueness without collisions.


Scaling:
    5. Scaling Considerations
    a. Database Sharding
    Distribute the URL data across multiple database shards based on the short URL ID or another sharding key.
    b. Caching
    Use a caching layer (e.g., Redis) to store recently accessed URLs to reduce database load.
    c. Rate Limiting
    Implement rate limiting on the API endpoints to prevent abuse and ensure fair usage.
    6. Security Considerations
    Validation: Ensure the long URL is a valid URL format before creating a short URL.
    HTTPS: Always use HTTPS to protect the data in transit.
    Expiration: Optionally allow users to set an expiration date for short URLs to improve security.
"""
