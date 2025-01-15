import math

def sine_f(n):
    r = 0
    for i in range(n):
        r = r + (math.sin(i/math.pi))
    return r

n = int(input("Enter the value of n:"))
d = sine_f(n)
print(d)