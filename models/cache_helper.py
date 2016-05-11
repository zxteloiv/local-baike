# coding: utf-8

import redis, random
from config import config

def get_redis():
    ip = random.choice(config['redis']['ip'])
    r = redis.StrictRedis(host=ip, port=config['redis']['port'], db=config['redis']['db'])
    return r

