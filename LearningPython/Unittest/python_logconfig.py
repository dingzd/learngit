# -*- coding:utf-8 -*-
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='report1.log',
    filemode='w'

)