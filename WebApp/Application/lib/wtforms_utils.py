from wtforms.validators import Optional, ValidationError, DataRequired
import os


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