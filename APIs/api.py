from flask import Flask
app = Flask(__name__) # Create a Flask application instance
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app) # Initialize SQLAlchemy with the Flask app
@app.route('/')
def index():
    return 'Hello!'
@app.route('/test')
def test():
    return {"message": "This is a test endpoint"}
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self): #representation 
        return f"{self.name} - {self.description}"


@app.route('/drinks')
def get_drinks():
    return {"drinks": ["Coffee", "Tea", "Juice"]}