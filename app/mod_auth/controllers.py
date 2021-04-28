from flask import Blueprint, request
from app import db
from app.mod_auth.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/')
def index():
  return {
    "users": [i.as_dict() for i in User.query.all()],
  }


@mod_auth.route('/user', methods=['POST'])
def create_user():
  data = request.get_json()
  user = User(
    full_name=data['full_name'],
    phone_number=data['phone_number'],
  )
  db.session.add(user)
  db.session.commit()
  return user.as_dict()


@mod_auth.route('/user/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dispatcher(id=None):
  user = User.query.get_or_404(id)

  if request.method == 'GET':
    return {"item": user.as_dict()}

  elif request.method == 'PUT':
    data = request.get_json()
    user.full_name = data['full_name']
    user.phone_number = data['phone_number']
    db.session.add(user)
    db.session.commit()
    return {"item": user.as_dict()}

  elif request.method == 'DELETE':
    db.session.delete(user)
    db.session.commit()

  return {"status": "ok"}
