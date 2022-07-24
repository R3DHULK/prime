n1=int(input("Enter Number : "))

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            print("Non-prime") 
            break
    else :
        print("Prime")
print(isprime(n1))