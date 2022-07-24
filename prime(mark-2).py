n1=int(input("Enter a number : "))
n2=int(input("Enter another : "))
import math
def is_not_prime(n):
    ans = False
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans
print("HULK is finding non-prime numbers : ")
for x in filter(is_not_prime, range(n1, n2)):
    print(x)
