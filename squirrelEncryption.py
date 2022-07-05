import string

chars = string.ascii_letters + string.digits + string.punctuation

def squirrel(password):
    listaCripto = []
    cont = 0
    cont2 = 0
    cont3 = 1
    passwordCripto = ''

    for j in password:
        if j in chars:
            for num, i in enumerate(chars):
                if j == i:
                    cont = int(ord(i)) + len(password)
                    cont2 = int(ord(i)) + len(password)
                    cont+=cont3
                    cont2+=cont3
                    cont+=cont2
                    
                    for k in range(len(password)):
                        if cont >= len(chars):
                            cont-=len(chars)
                        elif cont <= len(chars):
                            listaCripto.append(chars[cont])
                            break
        cont3+=1
    
    for i in listaCripto:
        passwordCripto+=i
    
    return print(passwordCripto)

squirrel(input('> '))