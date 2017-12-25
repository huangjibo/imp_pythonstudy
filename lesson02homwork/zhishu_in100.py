#写出100以内的所有质数：

from math import sqrt
j=2
while j<=100:
 i=2
 k=sqrt(j) #求j的平方根，一个数最大的因子不会大于自己的平方根
 while(i<=k): #从2到k测试是否为j的因子
     if j%i==0: #如果i是j的因素，退出循环
         break
     i=i+1
 if(i>k):  #如果没有中途退出循环，则i=i+1一直执行到i<=k不成立为止，j没有因数，是质素
     print(j) #则打印
 j=j+1 
