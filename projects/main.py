from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__,)

@main.route('/home')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, age=current_user.age)

@main.route('/cv')
@login_required
def cv():
    return render_template('cv.html', name=current_user.name)

