from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hell, PetFax'
    
    #register pet blueprint
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    return app