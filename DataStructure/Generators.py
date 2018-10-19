#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: Generators.py
# Author: Dixon
# Mail: cndixon@163.com
# Created Time: 2018/10/19


colors = ['black', 'red']
sizes = ['S', 'M', 'L']

# ((c, s) for c in colors for s in sizes)   was a Generator.
# <generator object <genexpr> at 0x000002D5C65385C8>

for t_shirt in ((c, s) for c in colors for s in sizes):
    print(t_shirt)

# ('black', 'S')
# ('black', 'M')
# ('black', 'L')
# ('red', 'S')
# ('red', 'M')
# ('red', 'L')
