from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# In terminal, navigate to the folder continaing this file and execute
# flask run
# then navigate a browser to http://127.0.0.1:5000/