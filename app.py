from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://tabekg:tabekg@localhost:5432/besoft_go_taxi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class DispatcherModel(db.Model):
  __tablename__ = 'tabekg_dispatchers'

  id = db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String, nullable=False)
  phone_number = db.Column(db.String, nullable=False)

  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

  def __init__(self, full_name, phone_number):
    self.full_name = full_name
    self.phone_number = phone_number

  def __repr__(self):
    return f"<Dispatcher {self.full_name}>"


@app.route('/')
def index():
  return {"dispatchers": [i.as_dict() for i in DispatcherModel.query.all()]}


@app.route('/dispatcher/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dispatcher(id=None):
  dispatcher = DispatcherModel.query.get_or_404(id)

  if request.method == 'GET':
    return {"item": dispatcher.as_dict()}

  elif request.method == 'PUT':
    data = request.get_json()
    dispatcher.full_name = data['full_name']
    dispatcher.phone_number = data['phone_number']
    db.session.add(dispatcher)
    db.session.commit()
    return {"item": dispatcher.as_dict()}

  elif request.method == 'DELETE':
    db.session.delete(dispatcher)
    db.session.commit()

  return {"status": "ok"}


if __name__ == "__main__":
  app.run(debug=True)
