# Time complexity => O(n) - optimised {O(n*log(log(n))) - Classic}
# Space complexity => O(n)

# Qn: Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

from math import sqrt

def countPrime(n):
    prime=[0 for x in range(n+1)] # Initialize a prime array with all values to "0"

    # Change the values of all the mul of "2" => 1
    for i in range(4,n+1,2):
        prime[i]=1
    
    # Iterate through all odd num until SQRT(N)
    for i in range(3,int(sqrt(n))+1,2):
        if prime[i]==0:
            # Change the values of all the mul of prime no => 1
            for j in range(i*i,n+1,i):
                prime[j]=1

    # Print the no. of prime in N 
    a=0
    for i in range(2,n+1):
        if prime[i]==0:
            a+=1
    print(a)

if __name__=="__main__":
    countPrime(25)
