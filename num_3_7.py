#! /usr/bin/python3m

num1=int(input("숫자를 입력하세요 : "))

if num1%3==0 and num1%7==0:
    print("3의 배수이자, 7의 배수입니다.")
elif num1%3==0:
    print("3의 배수입니다.")
elif num1%7==0:
    print("7의 배수입니다.")
else:
    print("아무것도 아닙니다.")
