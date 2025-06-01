#sum of the primes numbers bellow two million

#and now, i need to find the primes bellow a number
limit = 2*10**6
sum = 0

for x in range(2,limit):
    number = x
    dividers = 2
    #qualquer número e primo até que tenhas mais de 2 divisores
    #first i need to find the primes
    divisor = 2
    #the code is taking a lot of time to return the sum, so the fast way to do this is not operating all number bellow 
    if number %2 ==0 and number !=2:
        dividers = dividers +1
    if number % 3 ==0 and number !=3:
        dividers = dividers+1
    if number % 5 ==0 and number != 5:
        dividers = dividers +1
    if number % 7 ==0 and number !=7:
        dividers = dividers+1
    if number % 11 ==0 and number !=11:
        dividers = dividers +1
    if number %13 ==0 and number != 13:
        dividers = dividers +1
    if number %17 ==0 and number != 17:
        dividers = dividers +1
    if number %19 ==0 and number != 19:
        dividers = dividers+1
    if number %23 ==0 and number != 23:
        dividers = dividers +1
    if number %29 == 0 and number != 29:
        dividers = dividers +1
    if number %31 ==0 and number != 31:
        dividers = dividers+1
    if number %37 ==0 and number != 37:
        dividers = dividers+1
    if number %41 == 0 and number!= 41:
        dividers = dividers+1

    raizq = number**(1/2)#não precisa testar número menores que a raiz, regra dos divisores em par
    while divisor <= raizq and dividers <= 2: #if dividers >2 the number is not prime
        if number % divisor ==0:
            dividers = dividers +1
        divisor = divisor +1

    if dividers ==2:
        sum = sum + number
print('a soma de todos os primos abaixo de ', limit, 'é: ', sum)
