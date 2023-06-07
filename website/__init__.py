from flask import Flask

def create_app():
    app = Flask(__name__)   #name of the file (that is ran?) 
    app.config['SECRET_KEY'] = 'anything can go here just dont share it in real world'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')   #url prefix is "how do I access the views"
    app.register_blueprint(auth, url_prefix='/')    #if we put another string after backslash, it would be prefixed
    

    return app