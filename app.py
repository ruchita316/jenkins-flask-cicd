from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask CI/CD Pipeline is Working!"

@app.route("/about")
def about():
    return "Deployed automatically using Jenkins and Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
