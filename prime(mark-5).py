n1=int(input("Enter Number : "))
def isprime(num):
    if num==2 or num==3:
        return ("Prime")
    if num%2==0 or num<2:
        return ("Non-prime")
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return ("Non-prime")   
    return ("Prime")
print(isprime(n1))