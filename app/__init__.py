from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register main routes
    from . import routes
    app.register_blueprint(routes.bp)

    # Register admin routes
    from . import admin_routes
    app.register_blueprint(admin_routes.admin_bp)

    return app
