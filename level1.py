# Check if a number is prime

def prime(n):
    if n <= 1:
        return "not prime number"
    else:
        is_prime = True
        for i in range(2,n):
            if n%i == 0:
                is_prime = False
                break
        if is_prime:
            return "prime number"
        else:
            return "not prime number"

# accpept a number from the user asan input:

n = int(input("enter a number: "))
print(prime(n))
