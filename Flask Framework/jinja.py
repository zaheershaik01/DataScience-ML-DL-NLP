### Building URL Dynamically
### Variable Rule
### Jinja 2 Template Engine

## Jinja2 Template Engine 
'''
{{ }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI (Wev server Gateway Interface) application.
'''
### WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html', results=res)


## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score': score, "res": res}
    return render_template('result1.html', results=exp)


## if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results = score)


@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('result.html', results=score)

if __name__ == "__main__":
    app.run(debug=True)

