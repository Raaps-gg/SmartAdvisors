import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .config import Config
from .extensions import db, migrate

def create_app():
    # Load environment variables from .env
    load_dotenv()
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)
    app.config.from_object(Config)

    # Accept DATABASE_URL or SQLALCHEMY_DATABASE_URI
    db_url = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URI")
    if db_url:
        # Some providers give DATABASE_URL starting with postgres://
        # SQLAlchemy prefers postgresql://; the 'postgres://' scheme still often works, 
        # but we normalize it here just in case.
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/ping")
    def ping():
        return "pong", 200

    # simple route to show DB count
    @app.route("/users-count")
    def users_count():
        try:
            count = db.session.execute("SELECT COUNT(*) FROM \"user\";").scalar()
            return {"users": int(count)}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    # register models
    from . import models  # noqa

    from . import routes  # noqa
    app.register_blueprint(routes.api_bp)

    return app
