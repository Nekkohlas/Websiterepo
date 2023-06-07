#store standard route for pages the users can see

from flask import Blueprint, render_template # blueprint seperates app out, blueprint views allow to neatly organize app
import os

views = Blueprint('views', __name__)         #views is a blueprint and we pass views as name 

#define a view 

@views.route('/')           #inside route() is the url of the endpoint
def home():                 #this function will run, when the slash route is used, inside of home function shows
    return  render_template('home.html') 
