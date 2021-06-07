from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
	first_name = "John"
	return render_template("index.html", first_name=first_name)

# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

