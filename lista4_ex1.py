n = int(input())
soma = 0

# lista de números possíveis

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

qt_leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range (n):

    soma = 0

    v = input()
    
    for i2 in (v):

        for i3 in (numeros):

            if(i2 == i3):

                soma += qt_leds[numeros.index(i3)]

    print(soma, "leds")
    
        

    
        

        
