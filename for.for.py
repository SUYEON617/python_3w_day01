#! /usr/bin/python3m

for i in range(1,10):
    if i%2==0:
        print(i,"단 시작!")
        for x in range(1,10):
            print(i,"X",x,"=",i*x)



"""
for i in range(2,10,1):
    for j in range(1,10,1):
        if i %2 ==0:
            print(f"{i} X {j} = {i*j}") #f스트링
"""
