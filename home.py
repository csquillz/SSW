from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')

def home():

    return render_template('structure.html')

def hobby1():

    return render_template('hobby1.html')

if __name__ == '__main__':

    app.run(debug=True)