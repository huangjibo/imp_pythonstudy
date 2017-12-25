def fib3(a, b):
    print(a+b)
    
def fib2(a, b):
    print(a+b)
    fib3(b,a+b)

def fib1(a, b):
    print(a+b)
    fib2(b,a+b)

#fib1(1,1)
    


def fib(lim, level=1, a=1, b=0):#输出斐波那契数的前几位
    print(a+b)
    if level==lim:return
    fib(lim, level+1, b, a+b)

fib(10)
fib(10,1,1,0)

