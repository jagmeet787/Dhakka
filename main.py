import falcon

class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nHttp Response')

app = falcon.API()

main = MainResource()

app.add_route('/main', main)