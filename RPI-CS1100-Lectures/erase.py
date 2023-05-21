def gcd(a,b):
    if a < b:
        a,b = b,a

    r = a % b
    if r==0:
        return b
    else:
        return gcd(b,r)
    
print(gcd(36,24))
print(gcd(84,65))
print(gcd(84,66))
