# Time complexity => O(n*log(log(n)))
# Space complexity => O(n)


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