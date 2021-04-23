from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def mike():
    return render_template('about.html')

@app.route('/estimate', methods=['GET'])
def estimate():
    return render_template('estimate.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        height = int(request.form['height'])
        radius = int(request.form['radius'])
        pi = 3.14
        top = pi * radius ** 2  
        side = 2 * (pi * (radius * height) )
        inarea = top + side
        sqarea = inarea/144
        mcost = sqarea * 25
        lcost = sqarea * 15
        tcost = mcost + lcost
        tcost = "{:.2f}".format(tcost)
        print(tcost)
    return render_template('estimate.html', tCost = tcost)


if __name__ == '__main__':
    app.run(debug=True)

