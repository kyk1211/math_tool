# 기본계산기
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide_new(x, y):
    return x / y

def get_Median(x, y):
    return (x+y)/2

def get_Sum_ver2(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum