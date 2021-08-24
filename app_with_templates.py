from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


# you can set a variable from the url

@app.route('/hello/<username>')
def hello_user(username):
    return '<p>Hello, ' + username + "!</p>"


# render an html file

@app.route('/example')
def example():
    with open("example.html") as f:
        return f.read()


# BETTER WAY: render an html template, filling in values depending on what was requested

import pandas as pd

dat = pd.io.parsers.read_csv("cases.csv", index_col=0)
# dat
# d = dat.loc[2018]
# d
# d[0]
# d.index
# d[d.index[0]]

from flask import render_template

@app.route('/cases/<year>')
def cases(year):
    return render_template("cases.html", year=year, data=dat.loc[int(year)])

# (flask looks for "cases.html" in the "templates" folder)



# in a terminal, navigate to the folder that contain with this file and run the following two commands
# (with "export" rather than "set" if you're using Mac or Linux)
# set FLASK_APP=app_with_templates
# flask run
