import tornado.web
import config

import models.view_helper

class ViewHandler(tornado.web.RequestHandler):
    def get(self, viewid=None):
        content = models.view_helper.get_view_by_id(viewid, self.settings['crawled_data_path'])
        self.write(content)

