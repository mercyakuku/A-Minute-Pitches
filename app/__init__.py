from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()




# Instances of flask extensions
# Instance of LoginManager and using its methods
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()

def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    
    Args:
        config_name : name of the configuration to be used
    '''

    # Initialising application
    app = Flask(__name__)
    simple.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])


    # Initialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app