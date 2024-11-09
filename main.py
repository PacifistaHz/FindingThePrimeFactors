number=input("Enter a number: ")
number=int(number)

arrayPrimeFactors=list()

diveder=2
while number != 1:
    if number % diveder == 0:
        number = number / diveder
        arrayPrimeFactors.append(diveder)
        diveder-=1
    diveder+=1

print(*arrayPrimeFactors,sep='\n')