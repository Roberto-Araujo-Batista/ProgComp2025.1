#sum of the primes numbers bellow two million

#and now, i need to find the primes bellow a number
limit = 10000
sum = 0

for x in range(1,limit+1):
    number = x
    dividers = 0
    #first i need to find the primes
    divisor = 1
    #the code is taking a lot of time to return the sum, so the fast way to do this is not operating all number bellow 
    while divisor <= number and dividers <=2: #if dividers >2 the number is not prime
            if number % divisor == 0:
                dividers = dividers + 1
            print(divisor)
            divisor = divisor + 1

    if dividers ==2:
        sum = sum + number
print('a soma de todos os primos abaixo de ', limit, 'é: ', sum)

