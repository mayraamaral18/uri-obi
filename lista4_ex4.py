t = int(input())

for i in range (t):

    sheldon, raj = input().split(' ')

    if(sheldon == 'tesoura'):
        
        if (raj == 'Spock' or raj == 'pedra'):
       
            print("Caso #{}:".format(i+1), "Raj trapaceou!")

        elif (raj == sheldon):

            print("Caso #{}:".format(i+1), "De novo!")

        else:
            print("Caso #{}:".format(i+1), "Bazinga!")


    if(sheldon == 'papel'):
        
        if (raj == 'tesoura' or raj == 'lagarto'):
       
            print("Caso #{}:".format(i+1), "Raj trapaceou!")

        elif (raj == sheldon):

            print("Caso #{}:".format(i+1), "De novo!")

        else:
            print("Caso #{}:".format(i+1), "Bazinga!")

    if(sheldon == 'pedra'):
        
        if (raj == 'papel' or raj == 'Spock'):
       
            print("Caso #{}:".format(i+1), "Raj trapaceou!")

        elif (raj == sheldon):

            print("Caso #{}:".format(i+1), "De novo!")

        else:
            print("Caso #{}:".format(i+1), "Bazinga!")

    if(sheldon == 'lagarto'):
        
        if (raj == 'pedra' or raj == 'tesoura'):
       
            print("Caso #{}:".format(i+1), "Raj trapaceou!")

        elif (raj == sheldon):

            print("Caso #{}:".format(i+1), "De novo!")

        else:
            print("Caso #{}:".format(i+1), "Bazinga!")

    if(sheldon == 'Spock'):
        
        if (raj == 'lagarto' or raj == 'papel'):
       
            print("Caso #{}:".format(i+1), "Raj trapaceou!")

        elif (raj == sheldon):

            print("Caso #{}:".format(i+1), "De novo!")

        else:
            print("Caso #{}:".format(i+1), "Bazinga!")
