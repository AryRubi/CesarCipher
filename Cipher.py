#Un solo programa que encripta y desencripta

#Pregunta que quiere el usario hacer

while True:

    print(' ')
    print('Do you want to encrypt or decrypt?')
    print('To exit enter "Bye"')
    Do = input("Enter your answer: ")
    print(' ')

    answer = Do.lower()

    if answer == 'encrypt':
        #mensaje pero en numeros
        code = list()

        #Escribir mensaje
        mssg1 = input("Enter message: ")
        mssg = mssg1.lower()

        #Inserir numero de encriptacion
        while True:
            inc = float(input("Please enter encryption key: "))
            if inc > 25:
                print(' ')
                print('Please enter a value between 1 and 25')
                print(' ')
                continue
            elif inc < 1:
                print(' ')
                print('Please enter a value between 1 and 25')
                print(' ')
                continue
            else:
                inc = round(inc)
                break

        #Dividir letra por letra
        def split(mssg):
            return [char for char in mssg ]

        letras = split(mssg)

        #Diccionario del alfabeto
        abc = {0:" ", 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

        #Cambiar letras por numeros
        for letra in letras:
            for key, value in abc.items():
                if letra == value:
                    code.append(key)

        #Mensaje encriptado numericamente
        codecrypto = list()

        #Encriptar mensaje
        for i in code:
            if i == 0:
                crypto = i
            else:
                crypto = i + inc
            codecrypto.append(crypto)

        #Eliminar numeros que son mayores a 26
        for num in codecrypto:
            if num > 26:
                codecrypto[codecrypto.index(num)] = num - 26

        #Mensaje encriptado
        mssgletras = list()

        #Tranformar mensaje encriptado numericamente a letras
        for n in codecrypto:
            for key, value in abc.items():
                if n == key:
                    mssgletras.append(value)

        #Unir el mensaje encriptado
        mssgcrypto = "".join(mssgletras)

        print(' ')
        print(mssgcrypto)
        print(' ')

        continue

    elif answer == 'decrypt':
        #mensaje pero en numeros
        code = list()

        #Escribir mensaje
        mssg = input("Enter message: ")

        #Inserir numero de desencriptacion
        while True:
            inc = float(input("Please enter encryption key: "))
            if inc > 25:
                print(' ')
                print('Please enter a value between 1 and 25')
                print(' ')
                continue
            elif inc < 1:
                print(' ')
                print('Please enter a value between 1 and 25')
                print(' ')
                continue
            else:
                inc = round(inc)
                break

        #Dividir letra por letra
        def split(mssg):
            return [char for char in mssg ]

        letras = split(mssg)

        #Diccionario del alfabeto
        abc = {0:" ", 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

        #Cambiar letras por numeros
        for letra in letras:
            for key, value in abc.items():
                if letra == value:
                    code.append(key)

        #Mensaje desencriptado numericamente
        codecrypto = list()

        #Desencriptar mensaje
        for i in code:
            if i == 0:
                crypto = i
            else:
                sum = i - inc
                if sum == 0:
                     crypto = int("26")
                else:
                    crypto = i - inc

            codecrypto.append(crypto)

        #Eliminar numeros que son menores a 0
        for num in codecrypto:
            if num < 0:
                codecrypto[codecrypto.index(num)] = num + 26

        #Mensaje desencriptado
        mssgletras = list()

        #Tranformar mensaje desencriptado numericamente a letras
        for n in codecrypto:
            for key, value in abc.items():
                if n == key:
                    mssgletras.append(value)

        #Unir el mensaje desencriptado
        mssgcrypto = "".join(mssgletras)

        print(' ')
        print(mssgcrypto)
        print(' ')

        continue

    elif answer == 'bye':

        print(' ')
        print('Goodbye')
        print(' ')
        break

    else:
        print(' ')
        print('Please enter and write your option correctly: Encrypt/Decrypt')
        print(' ')
        continue
