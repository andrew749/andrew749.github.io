#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/andrew749.github.io/")

logging.info('pls')
from app import application
application.secret_key = 'ayy dank memes'
