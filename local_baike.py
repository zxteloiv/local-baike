#!/usr/bin/env python2

import inspect, sys, os
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(1, os.path.join(currentdir, 'libs'))

import tornado.ioloop
import tornado.web
import tornado.options
          
tornado.options.parse_command_line()  

from routes import urls
from config import config

from models.log_helper import setLogger

class BaikeApp(tornado.web.Application):
    def __placeholder__(self):
        pass

application = BaikeApp(urls, **config)

if __name__ == "__main__":
    application.listen(config['port'])
    tornado.ioloop.IOLoop.instance().start()
