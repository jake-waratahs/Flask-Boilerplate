from flask.ext.classy import FlaskView, route
from flask import render_template
from flask.ext import menu
from models import User

class WTFormsController(FlaskView):
    route_base = '/wtforms/'

    @menu.classy_menu_item('frontend.examples.forms', 'WTForms', order=14, 
        description='Create beautiful HTML forms using Python classes. WTForms '\
        'adds form validation for commonly used HTML form patterns.')
    def index(self):
        return render_template('frontend.examples/wtforms/index.html', is_form=True)

    @route('/form/', methods=['GET','POST'])
    def form(self):
        form = MyForm()
        validated = False
        if form.validate_on_submit():
            validated = True

        return render_template('frontend.examples/wtforms/form.html', 
            is_form=True, validated=validated, form=form)

    def database(self):
        form = UserForm(obj=User.query.first())
        validated = False
        if form.validate_on_submit():
            validated = True

        return render_template('frontend.examples/wtforms/database.html', 
            is_form=True, validated=validated, form=form)



from flask_wtf import Form
from wtforms import (
    TextField,
    validators,
    IntegerField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.ext.sqlalchemy.orm import model_form
from flask_boilerplate_utils.forms import Unique
from Application import app

class MyForm(Form):
    number_field = IntegerField('Number', [validators.Required()])
    text = TextField('Text Field', [validators.Required(), Unique(model=User, field=User.email)])
    password = PasswordField('Password', [validators.Optional()])
    submit = SubmitField('Submit', [validators.Optional()])
    toggle = BooleanField('Toggle', [validators.Optional()])

UserForm = model_form(User, db_session=app.db.session, base_class=Form, field_args={
})
# Override the password field to set it's type manually.
UserForm.password = PasswordField('Password')
UserForm.submit = SubmitField('Submit')
