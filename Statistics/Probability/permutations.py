import math

#total permutations of an N set
def permutation_original(n):
    return math.factorial(n)

#permutations of an N set (no repetition)
def permutation_norepetition(n,k):
    return math.factorial(n)/ math.factorial(n-k)

#permutations WITH repetition
def permutation_repetition(n,k):
    return k**n


