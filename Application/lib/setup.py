from models import (
    User, 
    Role
)
from flask.ext.security.utils import encrypt_password

def Setup(app, db):
    with app.app_context():
        db.create_all()
        if (len(User.query.filter_by(email='admin@localhost').all()) == 0):
            if len(Role.query.filter_by(name='admin').all()) == 0:
                # No user exists, create one.
                app.user_datastore.create_role(name="admin", description="Admin Users")
                app.user_datastore.create_user(email='admin@localhost', password=encrypt_password('admin'))
                db.session.commit()

                user = app.user_datastore.find_user(email='admin@localhost')
                role = app.user_datastore.find_role('admin')
                app.user_datastore.add_role_to_user(user, role)

                db.session.commit()