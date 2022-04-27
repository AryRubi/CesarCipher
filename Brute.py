
#Brute force a Cesar's Cipher

#Enter message
#Swap all the letters 25 times
#Give possible answers

abc = {0:" ", 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}


def Cipher ():
    inc = 0
    x = 1
    while inc < 26:
        #mensaje pero en numeros
        code = list()

        #Inserir numero de desencriptacion

        inc = inc + x

        #Dividir letra por letra
        def split(mssg):
            return [char for char in mssg ]

        letras = split(mssg)

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
        print('Key:',inc," ",mssgcrypto)

while True:

    print(" ")
    print('Please enter the message')
    print('To exit enter "Bye"')
    print(" ")
    message = input('')
    mssg = message.lower()

    if mssg == "bye":
        print(' ')
        print('Goodbye')
        print(' ')
        break
    else:
        Cipher()
        continue
