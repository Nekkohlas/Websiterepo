#store standard route for pages the users can see

from flask import Blueprint # blueprint seperates app out, blueprint views allow to neatly organize app

auth = Blueprint('auth', __name__)         #views is a blueprint and we pass views as name 

@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('sign-up')
def sign_up():
    return "<p>Sign Up</p>"