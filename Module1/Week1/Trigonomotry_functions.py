import math
import random

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def approx_sin(x,n):
    result = 0
    for i in range(n):
        result = result + pow(-1,i) * (pow(x,2*i+1) / factorial(2 * i + 1))
    return result

def approx_cos(x,n):
    result = 0
    for i in range(n):
        result = result + pow(-1,i) * (pow(x,2*i) / factorial(2 * i))
    return result


def approx_sinh(x,n):
    result = 0
    for i in range(n):
        result = result +  pow(x,2*i + 1) / factorial(2 * i + 1) 
    return result

def approx_cosh(x,n):
    result = 0
    for i in range(n):
        result = result +  pow(x,2*i) / factorial(2 * i) 
    return result

print(round(approx_cosh(3.14,10),2))