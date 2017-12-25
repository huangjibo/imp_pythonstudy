import os
os.mkdir('abc')  #创建了名为abc的文件夹

f=open('abc/abc.txt','w')
f.write('I love python!')
f.close()


f=open('abc/abc.txt')
print(f.readlines())
f.close()
