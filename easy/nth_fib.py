
def n_fib_rec(n):
     if n == 1:
        return 0
     elif n == 2:
         return 1
     
     return n_fib_rec(n-1) + n_fib_rec(n-2)


fib_dict = {1:0,2:1}
def n_fib_mem(n):

    try:
        return fib_dict[n]
    except:
        fib_dict[n] = n_fib_mem(n-1) + n_fib_mem(n-2)
        return fib_dict[n]


def n_fib_iter(n):
    fib_arr = [0,1]
    if n<=2:
        return fib_arr[n-1]
    
    i = 3
    while i<=n:
        next = fib_arr[0] + fib_arr[1]
        fib_arr[0] = fib_arr[1]
        fib_arr[1] = next
        i+=1

    return fib_arr[1]


n = 15


print("n_fib_rec = ",n_fib_rec(n))
print("n_fib_mem = ",n_fib_mem(n))
print("n_fib_iter = ",n_fib_iter(n))
