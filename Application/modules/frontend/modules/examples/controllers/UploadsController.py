from flask.ext.classy import FlaskView, route
from flask import render_template, flash
from flask.ext import menu

from ..uploads import uploads
import os

class UploadsController(FlaskView):
    route_base = '/uploads'

    @menu.classy_menu_item('frontend.examples.uploads', 'File Uploads', 
        order=13, description='Uploads made simple using Flask Uploads. ')
    @route('/', methods=['GET','POST'])
    def index(self):

        form = FileUploadForm()
        if form.validate_on_submit():
            filename = uploads.save(form.file_upload.data)
            flash("Uploaded %s" % (filename), 'success')

        # Spit out all the pre-existing uploaded images
        if not os.path.exists(uploads._config.destination):
            os.makedirs(uploads._config.destination)

        image_urls = map(uploads.url, os.listdir(uploads._config.destination))

        return render_template('frontend.examples/uploads/index.html', 
            is_form=True, image_urls=image_urls, form=form)
        
from flask_wtf import Form
from wtforms import (
    validators,
    SubmitField,
    FileField
)

from flask_boilerplate_utils.forms import ValidFileFormat

class FileUploadForm(Form):
    submit = SubmitField('Submit', [validators.Optional()])
    file_upload = FileField('Uploadable File', [
            validators.Required(), 
            ValidFileFormat(uploads) # Ensure the filetype is what is defined.
        ])