#计算n的阶乘的函数(n个对象进行排列)：
def fac(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(fac(9))

#n个对象里面选出m个出来进行排列：
def A(n,m):
    s=1
    for i in range(n-m+1,n+1):
        s*=i 
    return s
print (A(10,7))

#另一种计算n个对象里面选出m个出来进行排列的方法：
def A2(n,m):
    return fac(n)//fac(n-m)
print(A2(10,7))
print(A(10,7))

#计算从n个对象里选出m个进行组合的方法：
def C(n,m):
    return A(n,m)//fac(m)
def C2(n,m):
    return A2(n,m)//fac(m)
print(C(10,7))
print(C2(10,7))

        
    
