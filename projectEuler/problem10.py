#sum of the primes numbers bellow two million

#and now, i need to find the primes bellow a number
limit = 2*10**6
sum =0

for x in range(1,limit):
    number = x
    dividers = 0

#first i need to find the primes
    for divisor in range(1, number+1):
        if number % divisor == 0:
            dividers = dividers +1

    if dividers ==2:
        print(number)
        sum = sum + number
    
print(sum)