from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Web Data O'Mine Project<h1><h2>Admin Site<h2>"

if __name__ == "__main__":
    app.run()
