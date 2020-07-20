#! /usr/bin/python3m

n=int(input("숫자를 입력하세요: "))
result=1

while n<6:
    for i in range(1,n+1):
        result*=i
    print(result)
    break
