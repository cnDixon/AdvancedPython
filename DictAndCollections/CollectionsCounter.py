#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: CollectionsCounter.py
# Author: Dixon
# Mail: cndixon@163.com
# Created Time: 2018/10/19


from collections import Counter

"""
        字典 - 计数器
"""

ct = Counter(['a', 'a', 'b', 'a', 'c', 'b'])

print(ct)  # Counter({'a': 3, 'b': 2, 'c': 1})

ct = Counter('aaabbc')

print(ct)  # Counter({'a': 3, 'b': 2, 'c': 1})

print(ct.most_common(2))  # [('a', 3), ('b', 2)]
