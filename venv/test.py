import math
n = 8
fact = 1

# for i in range(1, n+1):
#     fact = fact*i
# print(fact)
#
# print(math.factorial(8))

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(3))

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n-1)
print(countdown(3))

def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)
string = input("Введите строку:")
ch = input("Введите букву для проверки:")
print(check(string,ch))

s = "12345"
print(s[0:4])

