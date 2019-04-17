import falcon
from falcon_multipart.middleware import MultipartMiddleware

from upload import UploadResource

api = application = app = falcon.API(middleware=[MultipartMiddleware()])

uploadResource = UploadResource()

app.add_route('/upload', uploadResource)