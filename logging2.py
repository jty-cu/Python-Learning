#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/11/23
@Auth: Eden Zhou
"""


import logging
logger = logging.getLogger('cn.cccb.tmplog') # 默认为logging.gerLogger('root')
logger.setLevel(logging.DEBUG)
# print(logger)
# print(type(logger))

## 处理器Handler
## 向控制台输出
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

## 向文件输出
## 没有制定日志级别，默认使用logger的日志级别（INFO）
fileHandler = logging.FileHandler(filename='demo2.log')
fileHandler.setLevel(logging.INFO)

## formatter 格式
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)s | %(message)s')  # 格式化format格式

## 串起来
## 1. 给处理器设置格式
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

## 2. 给记录器设置处理器
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


## 定义一个过滤器
flt = logging.Filter('cn.cccb') ## 根据logger的命名进行过滤，例如只输出以cn.cccb开头的logger的信息
## 关联过滤器
# logger.addFilter(flt) ## 空的，无输出，因为logger的名字现在是tmplog
fileHandler.addFilter(flt) ## console有输出，但是file中无输出



## print logs
logger.debug('this is debug') # 不会被输出。会以logger的设置为准（可以不设置logger的日志level）
logger.info('this is info')
logger.warning('this is warning')
logger.error('this is error')
logger.critical('this is critical')

'''
日志输出级别的继承关系：here, consoleHander and fileHander会继承logger的日志level
要实现consoleHander输出DEBUG level，fileHander输出INFO level，需要把logger.setLevel(logging.DEBUG), i.e. to the lowest level
'''




