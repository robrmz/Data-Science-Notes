import math

#Combinations WITH repetition
def combinations(n,k):
    return math.factorial(n)/ (math.factorial(n-k) * math.factorial(k))

    