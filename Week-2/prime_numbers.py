 
for prime_numbers in range(1,101):
    if prime_numbers > 1:
        for i in range(2,prime_numbers):
            if(prime_numbers % i) == 0:
                break
                
                    print(prime_numbers)