#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: MappingProxyType.py
# Author: Dixon
# Mail: cndixon@163.com
# Created Time: 2018/10/19


from types import MappingProxyType

"""
        不可变映射类型
        
        用 MappingProxyType 获取字典的只读实例
"""

_dict = {'version': '1.0', 'author': 'Dixon'}

_dict_proxy = MappingProxyType(_dict)

print(_dict_proxy)  # {'version': '1.0', 'author': 'Dixon'}

print(_dict_proxy['version'])  # 1.0

# _dict_proxy['version'] = '1.1'  # TypeError: 'mappingproxy' object does not support item assignment
