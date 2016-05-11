import tornado.web
import models.view_helper

class SubViewHandler(tornado.web.RequestHandler):
    def get(self, viewid=None, subviewid=None):
        content = models.view_helper.get_subview_by_ids(viewid, subviewid, self.settings['crawled_data_path'])
        self.write(content)
