#!/bin/bash

kill -9 `ps aux | grep local_baike.py | grep -v grep | awk '{print $2}'`
mkdir -p log
nohup python2 local_baike.py --log_file_prefix=log/access.log &>/dev/null &

