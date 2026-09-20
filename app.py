from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask CI/CD Project</h1><p>Application is running successfully!</p>"

@app.route("/about")
def about():
    return "<h2>About</h2><p>This is our Flask application for the MSE project.</p>"

if __name__ == "__main__":
    app.run(debug=True)