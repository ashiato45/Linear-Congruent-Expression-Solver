import math
#"Solve ax=b (mod c)

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solve(a, b, c):
    a = a % c
    b = b % c
    if gcd(a, c) != 1:
        return -1 # No answer
    else:
        for i in range(a):
            if (b + c*i) % a == 0:
                return (b + c*i) / a
        return -2 # Exception

print(solve(10, -5, 19))
print(solve(19*23, 1687598, 17))
print(solve(23*17, 2657854, 19))
print(solve(17*19, 3147558, 23))
print(solve(2, 109, 323))
print(solve(300, -2384, 7429))
print(solve(1151, 7493010, 7429))
print(solve(19*23, 1687598, 7429))
print(solve(730, 1, 2011))
