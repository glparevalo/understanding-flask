from flask import Flask

app = Flask(__name__)

# The '/' route, is the home page
# This function is a python decorator - gives additional functionality to a function
@app.route("/") # Called a syntactic sugar - syntax that makes it easier to write an alternative line of code
def hello_world():
    return "<p>Hello, World!</p>"

# This makes it possible for us to run main.py as a script
if __name__ == "__main__":
    app.run()