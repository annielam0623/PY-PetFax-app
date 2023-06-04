from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)

# database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ivan2010Lam@localhost:5432/petfax01'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    @app.route('/')
    def index():
        return 'Hell, PetFax'
    
    #register pet blueprint
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    return app