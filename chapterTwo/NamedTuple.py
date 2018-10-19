#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: NamedTuple.py
# Author: Dixon
# Mail: cndixon@163.com
# Created Time: 2018/10/19


from collections import namedtuple  # 具名元组

City = namedtuple('City', ['name', 'country'])

beijing = City('beijing', 'China')

print(beijing)          # City(name='beijing', country='China')

print(beijing.name)     # beijing
print(beijing.country)  # China
