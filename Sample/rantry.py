

#nums = [ [1,2,3],[4,5,6],[7,8,9]]
#cube_nums = [ j for i in nums for j in i]
#print(cube_nums)

def is_prime(n):
    '''This will return true if N prime'''
    if n < 2:
        return False
    for i in range(2, n// 2 + 1):
        if n % i == 0:
            return False
    return True

nums = [i for i in range(1,201)]
lst = list(filter(lambda i : i % 5 == 0 , nums))
#print(lst)

prime = list(filter(is_prime,nums))
print(prime)