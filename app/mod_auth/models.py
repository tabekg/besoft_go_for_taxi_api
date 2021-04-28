from app import db
import enum


class UserTypes(enum.IntEnum):
    taxi = 1
    dispatcher = 2


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def as_dict(self, items=None):
        if items is None:
            items = []
        response = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for i in items:
            response[i] = getattr(self, i).as_dict()
        return response


class User(Base):
    __tablename__ = 'tabekg_users'

    full_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False, unique=True)
    last_action = db.Column(db.DateTime, nullable=True)
    user_type = db.Column(db.Enum(UserTypes), default='taxi', nullable=False)

    def __init__(self, full_name, phone_number, last_action=None, user_type=None):
        self.full_name = full_name
        self.phone_number = phone_number
        self.last_action = last_action
        self.user_type = user_type

    def __repr__(self):
        return '<User %r>' % self.full_name
