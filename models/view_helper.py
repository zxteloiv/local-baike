import os.path
import json

def get_view_by_id(viewid, datapath):
    if viewid is None:
        return "404 not found"

    try:
        f = open(os.path.join(datapath, viewid + ".htm"))
        meta = json.loads(f.readline())
        data = f.read()
        return data
    except:
        return "500 server error"

def get_subview_by_ids(viewid, subid, datapath):
    if None in (viewid, subid):
        return "404 not found"

    try:
        f = open(os.path.join(datapath, str(viewid) + "_" + str(subid) + ".htm"))

        meta = json.loads(f.readline())
        data = f.read()
        return data
    except:
        return "500 server error"

