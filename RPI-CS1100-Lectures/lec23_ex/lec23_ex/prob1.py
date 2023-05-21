def recursive_add_impl(L):
    if len(L) ==0:
        return 0
    else:
        return L[0] + recursive_add_impl(L[1:])
    
def recursive_add(L):
    if len(L) == 0:
        return 0    # By convention
    if len(L) == 1:
        return L[0]
    else:
        return recursive_add_impl(L)

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))
