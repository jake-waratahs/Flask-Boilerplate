from Application import db, app
from flask.ext.security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def toDict(self):
        return dict(id=self.id, name=self.name, 
                    description=self.description)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def toDict(self):
        return dict(id=self.id, email=self.email, 
                    active=self.active, 
                    confirmed_at=self.confirmed_at,
                    roles=resultsToList(self.roles))

    def isAdmin(self):
        return self.has_role('admin')