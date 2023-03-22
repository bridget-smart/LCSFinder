import random
import numpy as np
import pandas as pd

   
from numba import jit, prange
import numpy as np
import warnings
from tqdm import tqdm
from ProcessEntropy.Preprocessing import tweet_to_hash_array


@jit(nopython=True, fastmath=True) 
def find_lambda_jit(target, source):
    """
    Finds the longest subsequence of the target array, 
    starting from index 0, that is contained in the source array.
    Returns the length of that subsequence + 1.
    
    i.e. returns the length of the shortest subsequence starting at 0 
    that has not previously appeared.
    
    Args:
        target: NumPy array, preferable of type int.
        source: NumPy array, preferable of type int.
    
    Returns:
        Integer of the length.
        
    """
    
    source_size = source.shape[0]-1
    target_size = target.shape[0]-1
    t_max = 0
    c_max = 0

    for si in range(0, source_size+1):
        if source[si] == target[0]:
            c_max = 1
            for ei in range(1,min(target_size+1, source_size - si+1)):
                if(source[si+ei] != target[ei]):
                    break
                else:
                    c_max = c_max+1

            if c_max > t_max:
                t_max = c_max 
                
    return t_max+1
@jit(nopython=True, parallel=True)
def get_all_lambdas(target, source, relative_pos, lambdas):
    """ 
    Finds all the the longest subsequences of the target, 
    that are contained in the sequence of the source,
    with the source cut-off at the location set in relative_pos.
    
    See function find_lambda_jit for description of 
        Lambda_i(target|source)
    
    Args:
        target: Array of ints, usually corresponding to hashed words.
        
        source: Array of ints, usually corresponding to hashed words.
        
        relative_pos: list of integers with the same length as target denoting the                                                               
            relative time ordering of target vs. source. These integers tell us the 
            position relative_pos[x] = i in source such that all symbols in source[:i] 
            occurred before the x-th word in target.  
            
        lambdas: A pre-made array of length(target), usually filled with zeros. 
            Used for efficiency reasons.
        
    Return:
        A list of ints, denoting the value for Lambda for each index in the target. 
    
    """
    i = 0
    while relative_pos[i] == 0: # Preassign first values to avoid check
        lambdas[i] = 1
        i+=1

    # Calculate lambdas
    for i in prange(i, len(target)):
        lambdas[i] = find_lambda_jit(target[i:], source[:relative_pos[i]]) 
            
    return lambdas


# ## FROM https://codegolf.stackexchange.com/questions/10701/fastest-code-to-find-the-next-prime - answer by primo
# # legendre symbol (a|m)
# # note: returns m-1 if a is a non-residue, instead of -1
# def legendre(a, m):
#     return pow(a, (m-1) >> 1, m)

# # strong probable prime
# def is_sprp(n, b=2):
#   d = n-1
#   s = 0
#   while d&1 == 0:
#     s += 1
#     d >>= 1

#   x = pow(b, d, n)
#   if x == 1 or x == n-1:
#     return True

#   for r in range(1, s):
#     x = (x * x)%n
#     if x == 1:
#       return False
#     elif x == n-1:
#       return True

#   return False

# # lucas probable prime
# # assumes D = 1 (mod 4), (D|n) = -1
# def is_lucas_prp(n, D):
#   P = 1
#   Q = (1-D) >> 2

#   # n+1 = 2**r*s where s is odd
#   s = n+1
#   r = 0
#   while s&1 == 0:
#     r += 1
#     s >>= 1

#   # calculate the bit reversal of (odd) s
#   # e.g. 19 (10011) <=> 25 (11001)
#   t = 0
#   while s > 0:
#     if s&1:
#       t += 1
#       s -= 1
#     else:
#       t <<= 1
#       s >>= 1

#   # use the same bit reversal process to calculate the sth Lucas number
#   # keep track of q = Q**n as we go
#   U = 0
#   V = 2
#   q = 1
#   # mod_inv(2, n)
#   inv_2 = (n+1) >> 1
#   while t > 0:
#     if t&1 == 1:
#       # U, V of n+1
#       U, V = ((U + V) * inv_2)%n, ((D*U + V) * inv_2)%n
#       q = (q * Q)%n
#       t -= 1
#     else:
#       # U, V of n*2
#       U, V = (U * V)%n, (V * V - 2 * q)%n
#       q = (q * q)%n
#       t >>= 1

#   # double s until we have the 2**r*sth Lucas number
#   while r > 0:
#       U, V = (U * V)%n, (V * V - 2 * q)%n
#       q = (q * q)%n
#       r -= 1

#   # primality check
#   # if n is prime, n divides the n+1st Lucas number, given the assumptions
#   return U == 0

# # primes less than 212
# small_primes = set([
#     2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
#    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
#    73, 79, 83, 89, 97,101,103,107,109,113,
#   127,131,137,139,149,151,157,163,167,173,
#   179,181,191,193,197,199,211])

# # pre-calced sieve of eratosthenes for n = 2, 3, 5, 7
# indices = [
#     1, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#    43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
#    89, 97,101,103,107,109,113,121,127,131,
#   137,139,143,149,151,157,163,167,169,173,
#   179,181,187,191,193,197,199,209]

# # distances between sieve values
# offsets = [
#   10, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6,
#    6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4,
#    2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6,
#    4, 2, 4, 6, 2, 6, 4, 2, 4, 2,10, 2]

# max_int = 2147483647

# # an 'almost certain' primality check
# def is_prime(n):
#   if n < 212:
#     return n in small_primes

#   for p in small_primes:
#     if n%p == 0:
#       return False

#   # if n is a 32-bit integer, perform full trial division
#   if n <= max_int:
#     i = 211
#     while i*i < n:
#       for o in offsets:
#         i += o
#         if n%i == 0:
#           return False
#     return True

#   # Baillie-PSW
#   # this is technically a probabalistic test, but there are no known pseudoprimes
#   if not is_sprp(n): return False
#   a = 5
#   s = 2
#   while legendre(a, n) != n-1:
#     s = -s
#     a = s-a
#   return is_lucas_prp(n, a)

# # next prime strictly larger than n
# def next_prime(n):
#     # return next prime strictly larger than n
#   if n < 2:
#     return 2
#   # first odd larger than n
#   n = (n + 1) | 1
#   if n < 212:
#     while True:
#       if n in small_primes:
#         return n
#       n += 2

#   # find our position in the sieve rotation via binary search
#   x = int(n%210)
#   s = 0
#   e = 47
#   m = 24
#   while m != e:
#     if indices[m] < x:
#       s = m
#       m = (s + e + 1) >> 1
#     else:
#       e = m
#       m = (s + e) >> 1

#   i = int(n + (indices[m] - x))
#   # adjust offsets
#   offs = offsets[m:]+offsets[:m]
#   while True:
#     for o in offs:
#       if is_prime(i):
#         return i
#       i += o


# def hash_uni(x,n):
#     a = 15
#     b = 9
#     m=2**16+1 # number of hashes
#     p=next_prime(m)

#     assert n>=1, 'n needs to be > 1'
#     return(((a*x+b)%p)%m)




# def tweet_to_h(tweet):
#     return [hash_uni(x,2) for x in tweet_to_hash_array(tweet)]