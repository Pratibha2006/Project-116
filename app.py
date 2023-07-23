from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Pratibha" 
    age = "16" 
    return render_template('index.html' , name = name , age = age)

app.run() 

@app.route("/father")
def father():
    return render_template('father.html')

@app.route("/mother")
def mother():
    return render_template('mother.html')

@app.route("/friend")
def friend():
    return render_template('friend.html')

app.run()