#! /usr/bin/python3m

import sys

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]} [numeric not zero]")
    sys.exit()

try:
    num=int(sys.argv[1])
    print(10/num)

except ValueError:
    print("input not valid")
    sys.exit() #뒤에 에러 나오지 않기 위해서
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
    sys.exit()

#한번에 쓰는 방법 
