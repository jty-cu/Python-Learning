#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/11/23
@Auth: Eden Zhou
"""

import logging
import logging.config

## 配置文件方式来处理日志

logging.config.fileConfig('logging.conf')

root_logger = logging.getLogger()
root_logger.debug('this is root logger, debug')

logger = logging.getLogger('applog')
logger.debug('this is applog, debug')

## 补充说明
a = 'abc'
try:
    int(a)
except Exception as e:
    # logger.error(e)
    logger.exception(e) ## 同时打印error和栈信息

## summary
# 1.编程式使用日志
# 2.logging格式的配置文件
# 3.字典方式的配置
logging.config.dictConfig({'loggers': 'root, applog'}) ## 配置文件格式：yml?, json