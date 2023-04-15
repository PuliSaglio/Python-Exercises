#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

numero = int(input('Digite um numero: '))

if numero % 2 ==  0:
    print(f'{numero} é par')
elif numero % 2 == 1:
    print(f'{numero} é impar')


#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
dividindo = float(input('Digite um numero a ser dividido: '))
divisor = float(input('Digite um divisor: '))

if dividindo % divisor == 0:
    print(f'A divisao entre {dividindo} e {divisor} dá um numero inteiro')
else:
    print(f'A divisao entre {dividindo} e {divisor} dá um numero racional')

print(f'O resultado é: {dividindo/divisor}')