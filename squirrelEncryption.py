import string

chars = string.ascii_letters + string.digits + string.punctuation

def squirrel(password):
    listaCripto = []
    cont = 1
    passwordCripto = ''

    for j in password:
        if j in chars:
            for i in chars:
                if j == i:
                    calc = int(ord(i))+len(password)+cont + int(ord(i))+len(password)-(cont*-1)
                    
                    for k in range(len(password)*10):
                        if calc >= len(chars):
                            calc-=len(chars)
                        elif calc <= len(chars):
                            print(calc)
                            listaCripto.append(chars[calc])
                            print(listaCripto)
                            break
        cont+=1
    
    for i in listaCripto:
        passwordCripto+=i
    
    return print(passwordCripto)

squirrel(input('> '))