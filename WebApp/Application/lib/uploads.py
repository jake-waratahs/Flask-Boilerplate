from flask.ext.uploads import (
    UploadSet,
    configure_uploads,
    UploadConfiguration,
    patch_request_class,
    IMAGES
)

# Stores CYO Creations
allowed = ('png', 'jpg', 'jpeg', 'TIFF', 'tiff')
main_uploads_config = UploadConfiguration('./Application/static/uploads/',
                                 base_url='/static/uploads/',
                                 allow=allowed,
                                 deny=())

main_uploads = UploadSet('mainuploads', allowed)
main_uploads._config = main_uploads_config

def configure_uploads(APP):
	with APP.app_context():
		# Allow Uploads of up to 32 MB.
		patch_request_class(APP, 32 * 1024 * 1024)
