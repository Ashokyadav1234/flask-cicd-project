from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {
        "name": "Python Mastery",
        "category": "Programming",
        "price": 799,
        "description": "Learn Python from basics to advanced concepts."
    },
    {
        "name": "AWS Cloud Basics",
        "category": "Cloud Computing",
        "price": 999,
        "description": "Learn the fundamentals of AWS and cloud computing."
    },
    {
        "name": "Machine Learning",
        "category": "Artificial Intelligence",
        "price": 1299,
        "description": "Understand machine learning algorithms and applications."
    },
    {
        "name": "Full Stack Development",
        "category": "Web Development",
        "price": 1099,
        "description": "Learn frontend and backend web development."
    }
]


@app.route("/")
def home():
    return render_template("index.html", courses=courses)


@app.route("/about")
def about():
    return """
    <h1>About CourseHub</h1>
    <p>CourseHub is an online learning platform for technology courses.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)