from Application.models.User import User
from Application.models.Role import Role
from Application import app, db, user_datastore
from flask.ext.security.utils import encrypt_password

def configure_app():
    with app.app_context():
        db.create_all()

        if (len(User.query.filter_by(email='admin@localhost').all()) == 0):
            if len(Role.query.filter_by(name='admin').all()) == 0:
                # No user exists, create one.
                user_datastore.create_role(name="admin", description="Admin Users")
                user_datastore.create_user(email='admin@localhost', password=encrypt_password('admin'))
                db.session.commit()

                user = user_datastore.find_user(email='admin@localhost')
                role = user_datastore.find_role('admin')
                user_datastore.add_role_to_user(user, role)

                db.session.commit()