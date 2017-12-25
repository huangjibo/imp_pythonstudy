print('请输入水位：')
level=input()

#洗衣流程
if level=='low':
    print('注水 20 L')
    print('搅拌30min')

if level =='high':
    print ('放水')
#甩干
print('请输入甩干次数：')
times=int(input())
for i in range (times):
    print('注入清水30L')
    print('搅拌 20min')
    print('放水')
    print('高速搅拌')
