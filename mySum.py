#! /usr/bin/python3m
"""
def mySum(x,y):
    print("%s + %s = %s"% (x,y,x+y))
#    print("x와 y의 합은" ,x+y)

"""


def mysum(x:int, y:int) -> int: #return 값이 int다
    return x+y 
#    print("%d + %d = %d"%(x,y,x+y))
#    print(f"{x} + {y} ={x+y}") #f 스트링 사용 예


a=int(input("x 값을 입력하세요 : "))
b=int(input("y 값을 입력하세요 : "))
#mySum(a,b)
print(mysum(a,b))
