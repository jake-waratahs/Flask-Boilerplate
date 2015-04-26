from flask.ext import uploads
# Configure file uploads for this blueprint.
allowed = ('tiff',) + uploads.IMAGES
_config = uploads.UploadConfiguration('./Application/static/uploads/',
                                 base_url='/static/uploads/',
                                 allow=allowed,
                                 deny=())
uploads = uploads.UploadSet('mainuploads', allowed)
uploads._config = _config