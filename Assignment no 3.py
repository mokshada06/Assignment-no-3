#3 Task no 1

n=int(input('enter a no: '))
def fact(n):
    if n < 2:
        return 1
    else:
        return n * (fact(n-1))
result=fact(n)
print('Factorial of no is: ',result)

Output:
enter a no:  10
Factorial of no is:  3628800


#3 Task no 2

import math

x= int(input('enter a no: '))

def sqrt(x):
    return (math.sqrt(x))
def log(x):
    return (math.log10(x))
def sin(x):
    return (math.sin(x))

result1 =sqrt(x)
print('Square Root: ',result1)
result2 =log(x)
print('Logarithm: ',result2)
result3 =sin(x)
print('Sine: ',result3)

Output:
