from wtforms.validators import Optional, ValidationError
import os
from Application.models.User import User

class ValidFileFormat(Optional):
    def __init__(self, fileupload, *args, **kwargs):
        self.fileupload = fileupload
        self.message = 'The selected file cannot be uploaded. Only %s are allowed.' % (', '.join(fileupload._config.allow))
        if 'message' in kwargs:
        	self.message = kwargs['message']

    def __call__(self, form, field):
    	filename, extension = os.path.splitext(field.data.filename)
    	if not self.fileupload.extension_allowed(extension[1:]):
    		raise ValidationError(self.message)

def email_available(form, field):
        if User.query.filter(User.email == field.data).first():
            raise ValidationError('A user with this email address already exists, email addresses must be unique.')
