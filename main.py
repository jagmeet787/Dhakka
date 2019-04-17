import falcon
from falcon_multipart.middleware import MultipartMiddleware
import io
import os
import shutil

class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nHttp Response')

    def on_post(self, req, resp):
    	apk = req.get_param('apk')
    	raw = apk.file.read()
    	if apk.filename:
    		filename = apk.filename
    		open(filename, 'wb').write(raw)
    	resp.status = falcon.HTTP_201

api = application = app = falcon.API(middleware=[MultipartMiddleware()])

main = MainResource()

app.add_route('/main', main)