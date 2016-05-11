import tornado.web

class ViewHandler(tornado.web.RequestHandler):
    def get(self, viewid=None):
        self.write("hello view")

