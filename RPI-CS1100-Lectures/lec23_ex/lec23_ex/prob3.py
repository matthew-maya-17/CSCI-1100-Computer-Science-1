
def fib(n):
    prev2 = 0
    prev1 = 0
    num = 1
    
    if n == 0:
        return 0
    
    for x in range(n-1):
        
        prev2 = prev1
        prev1 = num
        num = prev2 + prev1
        
    return num


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
