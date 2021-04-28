from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'tabekg_users'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(192), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


class Dispatcher(db.Model):
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