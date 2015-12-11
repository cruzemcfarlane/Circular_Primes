#Function to count the number of digits in 'n'
def digit(n):
    #Function to remove the last digit of 'n'
    def helper(x,ten):
        if x>=ten:
            return x/ten
        else:
            return 0

    if (n<10):
        return 1
    elif (n<1):
        return 0
    else:
        #Loop until all digits are counted
        return digit(helper(n,10))+1 


#Function to perform a single digit left circular shift
def lcs(n):
    if n<1:
        return False
    elif (n>0) and (n<10):
        return n

    else:
        last_digit=n%10
        allbutlast_digit=n/10

        #Convert integers to string
        last_digit=str(last_digit)
        allbutlast_digit=str(allbutlast_digit)

        #Concatenate strings
        con=last_digit+allbutlast_digit

        #Convert strings back to integer
        con=int(con)

        n=con
        return n

#Function to check if 'n' is prime
def isPrime(n):
    if n<2:
        return False
    else:
        for count in range(2,n):
            if (n%count == 0):
                return False                                   
        return True

#Function to check if the prime number is circular or not
def isCircular(n):
    #stop=digit(n) #Stop the loop when the left circular shifts are complete

    def helper(n,start,stop):
        if isPrime(n)==False:
            return False

        #Loop until circular shit is complete
        elif start <= stop:
            n=lcs(n)
            start+=1
            return helper(n,start,stop)
        else:
            return True
    if n<1:
        return False
    else:
        return helper(n,1,digit(n))

#Function to check the no. of circular primes blow 'n' 
def nbrCirPrimes(n):
    SumOfPrimes=0
    if n<2:
        return 'No circular primes in this range'
    else:
        for count in range(2,n):
            if (isPrime(count)==True) and (isCircular(count)==True):
                SumOfPrimes+=1
        return SumOfPrimes
