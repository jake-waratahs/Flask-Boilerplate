from flask.ext.uploads import (
    UploadSet,
    UploadConfiguration,
    patch_request_class,
    IMAGES
)

# Use lowercase only.
allowed = ('png', 'jpg', 'jpeg', 'tiff')
# Or
# Using flask_uploads's own types
# allowed = IMAGES

main_uploads_config = UploadConfiguration('./Application/static/uploads/',
                                 base_url='/static/uploads/',
                                 allow=allowed,
                                 deny=())

main_uploads = UploadSet('mainuploads', allowed)
main_uploads._config = main_uploads_config

def Uploads(app):
	with app.app_context():
		patch_request_class(app, 32 * 1024 * 1024)
