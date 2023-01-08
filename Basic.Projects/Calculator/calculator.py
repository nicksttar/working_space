"""Documentation and How it works:
Funtions: sum, minus, xxx, dell
Special commands:
restart - to restart Calculator
back - to quit Calculator
Example How it works:
1
+
2
3
"""


from calc import *
from sys import exit
from string import digits


def restb(s):  #check command and run it
    if s == "restart":
        print("Calculator was restarted")
        script(restb(input()))
    if s == "back":
        exit()
    else:
        return s


def validation(a, b, c):  #validation
    if a.isdigit() and b in "+-*/" and c.isdigit():
        return True
    return False

print("----------------")
print("Calculator v1.0")

def script(a):  #basic script
    while True:
        b = input()
        restb(b)
        c = input()
        restb(c)
        if validation(a, b, c) == True:
            n = Calculator(a, b, c)
        else:
            print("Something wrong try again")
            script(restb(input()))

        if b == "+":
            a = n.plus()
            print(a)
        elif b == "-":
            a = n.minus()
            print(a)
        elif b == "*":
            a = n.xxx()
            print(a)
        elif b == "/":
            a = n.dell()
            print(a)
        elif b == "%":
            pass


a = restb(input())
script(a)  #script call
