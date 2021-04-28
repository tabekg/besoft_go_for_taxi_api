from flask import Blueprint, request
from app import db
from app.mod_auth.models import Dispatcher

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/')
def index():
  return {"dispatchers": [i.as_dict() for i in Dispatcher.query.all()]}


@mod_auth.route('/dispatcher/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dispatcher(id=None):
  dispatcher = Dispatcher.query.get_or_404(id)

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