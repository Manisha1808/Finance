from flask import Flask
from config import Config
from database.db import db
from flask_cors import CORS

from routes.record_routes import record_bp
from routes.dashboard_routes import dashboard_bp
from routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ FIX: Apply CORS here
    CORS(app)

    db.init_app(app)

    app.register_blueprint(record_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(user_bp)

    @app.route("/")
    def home():
        return "Finance Backend Running"

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)