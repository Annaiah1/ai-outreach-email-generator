from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_email(company, role, industry):

    openings = [
        "I hope you're doing well.",
        "Greetings from our team!",
        "Hope this message finds you well.",
        "I wanted to reach out regarding an opportunity."
    ]

    values = [
        "help streamline operations",
        "boost productivity",
        "increase revenue growth",
        "optimize workflow efficiency",
        "enhance business performance"
    ]

    closings = [
        "Looking forward to your thoughts.",
        "Let’s connect and discuss further.",
        "Happy to schedule a quick call.",
        "Would love to explore this with you."
    ]

    email = f"""
Dear {company} Team,

{random.choice(openings)}

We specialize in helping {industry} organizations to {random.choice(values)}.
I believe our solutions can add value to your {role} initiatives.

{random.choice(closings)}

Best regards,  
Your Name
"""

    return email


@app.route("/", methods=["GET", "POST"])
def home():
    email = ""

    if request.method == "POST":
        company = request.form["company"]
        role = request.form["role"]
        industry = request.form["industry"]

        email = generate_email(company, role, industry)

    return render_template("index.html", email=email)


if __name__ == "__main__":
    app.run()
