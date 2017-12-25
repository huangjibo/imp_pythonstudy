print('需要写出斐波那契数列的前多少位？')
n=int(input())
s0=0
s1=1
print(s1)
for i in range (1,n+1):
    s0=s0+s1
    s1=s1+s0
    
    i=i+1
    print(s0)
    print(s1)
