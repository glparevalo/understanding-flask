from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This makes it possible for us to run main.py as a script
if __name__ == "__main__":
    app.run()