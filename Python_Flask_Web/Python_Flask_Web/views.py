"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Python_Flask_Web import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        'index.html',
        title='Home Page',
        )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')
