print('1+2+3...+100')
s=0
for i in range(101):
    s+=i #s=s+i
print(s)

print('1-100之间能被100整除的数')
for i in range(1,101):
      if 100%i==0:
           print(i)

print('1-100之间能被100整除的数 前4个')
s=0
for i in range(1,101):
      if 100%i==0:
           print(i)
           s+=1
           if s==4:break
           

print('1-100之间，个位和十位相加等于9的偶数：')
for i in range(1,101):
      if i%10+i//10==9 and i%2==0:#i%2!=0
          print(i)
      
print('1-100之间，个位和十位相加等于9的偶数： 前3个')
s=0
for i in range(1,101):
    if i%2!=0:continue
    if i//10+i%10==9:
        print(i)
        s+=1
        if s==3:break
        
