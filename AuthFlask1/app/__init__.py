import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configuración de la base de datos
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Crear carpeta instance si no existe
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Registrar db
    from . import db
    db.init_app(app)

    # Ruta simple de prueba
    @app.route('/')
    def home():
        return "Hello, Flaskr!"
    
    #agregamos blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    return app
