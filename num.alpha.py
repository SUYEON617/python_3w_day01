#! /usr/bin/python3m

x=input("값을 입력하세요 : ")

if x.isalpha():
    print(f"{x}는 문자")
elif x.isnumeric():
    print(f"{x}는 숫자")
else:
    print("?")
