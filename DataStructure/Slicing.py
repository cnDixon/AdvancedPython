#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: Slicing.py
# Author: Dixon
# Mail: cndixon@163.com
# Created Time: 2018/10/19


"""
        切片
"""

"""

可以使用 s[a:b:c] 的形式对s在a和b之前以c为间隔取值
c的值还可以为负, 负值意味着反向取值。

        seq[start:stop:step]

"""

s = 'bicycle'

print(s[::3])  # bye
print(s[::-1])  # elcycib
print(s[::-2])  # eccb
print(s[1:-2:2])  # icyc -> iy
