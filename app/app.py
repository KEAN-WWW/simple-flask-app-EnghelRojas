"""
This script is a simple Flask application with multiple routes and template rendering.
"""

from flask import Flask, render_template

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    """Displays the default welcome message."""
    return "Hello CPS3500!"

# Route for new page
@app.route('/new_page')
def new_page():
    """Displays the content for the new page."""
    return "This is a New Page!"

# Route for user page with dynamic variable
@app.route('/user/<username>')
def greet_user(username):
    """
    Displays a greeting for the user.

    If the username is 'jack', it greets with uppercase.
    Otherwise, it displays a default anonymous message.
    """
    return render_template('greeting.html', user=username)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
