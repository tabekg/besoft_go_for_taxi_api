from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.errorhandler(404)
def not_found(error):
    return {"status": "not_found", "result": -1}, 404


from app.mod_auth.controllers import mod_auth as auth_module

app.register_blueprint(auth_module)

db.create_all()
