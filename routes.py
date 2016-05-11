
# apis
from controllers.view import ViewHandler
from controllers.subview import SubViewHandler

# url routing
urls = [
    (r"/view/(\d+).html?", ViewHandler),
    (r"/subview/(\d+)/(\d+).html?", SubViewHandler),
]


