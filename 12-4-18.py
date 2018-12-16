#Coding Prime Number Assignment together
import sys
countPrimes = 0
start = int(input("Give me a low number: "))
stop = int(input("Give me a high number: "))
if (stop <= start):
    print("Make sure your low number is smaller than your high number!")
    sys.exit()
for current in range(stop,start-1, -1):
    print("\nCurrent: " + str(current))
    print("Divisors: ", end="")
    countDivisors = 0
    for divisor in range(1, current+1):
        if (current % divisor) == 0:
            countDivisors = countDivisors + 1
            print(str(divisor) + " ", end="")
    if(countDivisors <= 2):
        print("- Prime Number", end="")
        countPrimes = countPrimes + 1
    print("")
print("Total Primes = " + str(countPrimes))
