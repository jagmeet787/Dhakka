import falcon
from falcon_multipart.middleware import MultipartMiddleware
# from falcon_cors import CORS 
from upload import UploadResource

# cors = CORS(allow_origins_list=['*://*/*']) 
api = application = app = falcon.API(middleware=[MultipartMiddleware()])

# public_cors = CORS(allow_all_origins=True)


# class ThingsResource(object):
# 	cors = public_cors
#     def on_get(self, req, resp):
#         resp.status = falcon.HTTP_200  # This is the default status
#         resp.body = ('\nTwo things\n')

class StaticResource(object):
	# cors = public_cors
    def on_get(self, req, resp, filename):
        # do some sanity check on the filename
        print filename
        if(filename == ''):
        	filename = 'index.html'
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open(filename, 'r') as f:
            resp.body = f.read()


class ImageResource(object):
	# cors = public_cors
    def on_get(self, req, resp, filename):
    	if(filename == ''):
        	filename = '24.gif'
        filename = 'image/' + filename
        print filename
        resp.status = falcon.HTTP_200
        resp.content_type = 'image/gif'
        with open(filename, 'r') as f:
            resp.body = f.read()

upload_resource = UploadResource()
# t_res = ThingsResource()
static_resource = StaticResource()
image_resource = ImageResource()

app.add_route('/upload', upload_resource)
# app.add_route('/test', t_res)
app.add_route('/{filename}', static_resource)
app.add_route('/image/{filename}', image_resource)