from flask import Flask, render_template
from flaskr import app

app = Flask(__name__)  

@app.route('/')

def home():

    return render_template('structure.html')

@app.route('/hobby1')

def hobby1():

    return render_template('hobby1.html')

@app.route('/hobby2')

def hobby2():

    return render_template('hobby2.html')

@app.route('/hobby3')

def hobby3():

    return render_template('hobby3.html')

@app.route('/hobby4')

def hobby4():

    return render_template('hobby4.html')

@app.route('/hobby5')

def hobby5():

    return render_template('hobby5.html')

@app.route('/hobby6')

def hobby6():

    return render_template('hobby6.html')

@app.route('/hobby7')

def hobby7():

    return render_template('hobby7.html')

@app.route('/hobby8')

def hobby8():

    return render_template('hobby8.html')

@app.route('/hobby9')

def hobby9():

    return render_template('hobby9.html')

@app.route('/hobby10')

def hobby10():

    return render_template('hobby10.html')

if __name__ == '__main__':

    app.run(debug=True)