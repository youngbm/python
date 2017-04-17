#!/usr/bin/dev python
#coding=utf-8

import json

yg=dict(name='yg', ceo_name='tiger', emp_num=100)

print("BEFORE")
j_yg=json.dumps(yg)
print(type(j_yg),":\n", j_yg)
print(type(yg), ":\n", yg)

print("AFTER")
d_yg=json.loads(j_yg)
print(type(d_yg),":\n", d_yg)
print(type(yg), ":\n", yg)