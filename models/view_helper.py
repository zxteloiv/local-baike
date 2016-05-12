import os.path
import json
from models.cache_helper import get_redis
from config import config

def load_file_as_view(filename):
    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    try:
        with open(filename) as f:
            meta = json.loads(f.readline())
            data = f.read()
            return (meta, data)
    except:
        return (None, None)

def build_path(viewid, subviewid=None):
    r = get_redis()
    key = viewid + ("" if subviewid is None else "_" + subviewid) + ".htm"
    data = r.get(key)
    if data is None:
        return None

    return os.path.join(config['crawled_data_path'], data)

def get_view_by_id(viewid):
    if viewid is None:
        return "404 not found"

    filename = build_path(viewid)
    if filename is None:
        return "filename err viewid=%s" % viewid

    meta, data = load_file_as_view(filename)
    
    if meta is None:
        return "500 server error"
    else:
        return data

def get_subview_by_ids(viewid, subid):
    if None in (viewid, subid):
        return "404 not found"

    filename = build_path(viewid, subid)
    if filename is None:
        return "filename err viewid=%s subid=%s" % (viewid, subid)

    meta, data = load_file_as_view(filename)

    if meta is None:
        return "500 server error"
    else:
        return data

