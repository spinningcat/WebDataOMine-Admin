from flask import Flask
import sys

port = 8080 if len(sys.argv) > 1 and sys.argv[1] == "dev" else 80
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Web Data O'Mine Project<h1><h2>Admin Site<h2>"


if __name__ == "__main__":
    print("Listening port " + str(port))
    app.run(port=port)
