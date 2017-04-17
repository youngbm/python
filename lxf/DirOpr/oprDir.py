#!/usr/bin/dev python
#coding= utf-8

import os

absPath=os.path.abspath('..')
print(absPath)

creatPath=os.path.join(r'E:\myGit\python\lxf', 'CoreIO')
print(creatPath)

os.mkdir('testdir')
os.rename('testdir', 'testdir2')
os.rmdir('testdir2')

testpaht = os.path.split('/Users/michael/testdir/file.txt')
print(testpaht[1])

#分离后缀
os.path.splitext('/path/to/file.txt')

# list abspath dirfile
dirList=[i for i in  os.listdir(absPath)  if os.path.isdir(os.path.join(absPath, i))]
fileList=[i for i in  os.listdir(absPath)  if os.path.isfile(os.path.join(absPath, i))]

print("dir:", dirList)
print("file:", fileList)




