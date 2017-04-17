#!/usr/bin/dev python


from io import StringIO


f=StringIO()
f.write('hahahahayy')
f.write('hahahahayy')
f.write('hahahahayy')

print(f.getvalue())