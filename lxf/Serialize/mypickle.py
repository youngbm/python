#!/usr/bin/dev python

import pickle


xzy=dict(name='xiezhiyang', sex='f', age=27)
p_xzy=pickle.dumps(xzy)
print(p_xzy)

s_xzy=pickle.loads(p_xzy)
print(s_xzy)

fjh=dict(name='fanjiahui', sex='m', age=26)

with open('pickle_s.txt', 'wb') as f:
    p_fjh=pickle.dump(fjh, f)
    f.close()
    #print(p_fjh)
    
with open('pickle_s.txt', 'rb') as f2:
    s_fjh=pickle.load(f2)
    f2.close()
    print(s_fjh)