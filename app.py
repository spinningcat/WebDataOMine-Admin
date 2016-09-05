from flask import Flask
import sys

devMode = len(sys.argv) > 1 and sys.argv[1] == "dev"
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Web Data O'Mine Project<h1><h2>Admin Site<h2>"


if __name__ == "__main__":
    if devMode:
        app.run(port=8080)
    else:
        app.run(port=80)
