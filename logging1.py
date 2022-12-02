#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/11/23
@Auth: den Zhou
"""

import logging
## PART I
## 默认的日志输出级别：warning
## 使用 baseConfig()来指定日志输出的级别
## param: filemodel: w: clear all and rewrite; a: continue writing

logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)

logging.debug('this is a debug log')
logging.info('this is a info log')
logging.warning('this is a warning info')
logging.error('this is an error info')
logging.critical('this is a critical info')


## PART II
## 向日志输出变量
name = 'alice'
age = 18
logging.basicConfig(level=logging.DEBUG)
logging.debug('name %s, age %d', 'alice', 18)
logging.debug('name %s, age %d' %('alice', 18))
logging.debug('name {}, age {}'.format('alice', 18))
logging.debug(f'name {name}, age {age}')


## 输出格式和添加公共信息
'''
format='%(xxxxx)-Ns', N：占位符，-：左对齐（没有表示右对齐）
format='%(message)s': 输出信息
format='%(asctime)s': 时间
format='%(levelname)s': 日志等级
format='%(filename)s:%(lineno)s': 文件名和行数
datefmt='%Y-%m-%d %H:%M:%S': 按照想要的时间格式输出
'''

name = 'alice'
age = 18
logging.basicConfig(format='%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
logging.debug('name %s, age %s', name, age)
logging.info('name %s, age %s', name, age)



