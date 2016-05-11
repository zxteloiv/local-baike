import tornado.web

class SubViewHandler(tornado.web.RequestHandler):
    def get(self, viewid=None, subviewid=None):
        self.write("hello subview")
