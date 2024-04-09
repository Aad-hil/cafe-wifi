# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import CreateAddReviewForm
from flask_bootstrap import Bootstrap
# Initialize Flask app
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes1.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize SQLAlchemy
db = SQLAlchemy()
db.init_app(app)


# Define Cafe model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    wifi_strength = db.Column(db.String(20), nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=False)


# Define Review model


with app.app_context():
    db.create_all()


# Home route
@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)


# Add cafe route
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CreateAddReviewForm()
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        wifi_strength = request.form['wifi_strength']
        seating_capacity = request.form['seating_capacity']
        new_cafe = Cafe(name=name, location=location, wifi_strength=wifi_strength,
                        seating_capacity=seating_capacity)
        db.session.add(new_cafe)
        db.session.commit()
        flash('Cafe added successfully!')
        return redirect(url_for('home'))
    return render_template('add_cafe.html')


if __name__ == '__main__':

    # db.create_all()  # Create database tables
    app.run(debug=True)
