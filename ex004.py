a = input('digite algo? ')
print(type(a))
print('ele é alfabetico? {}' .format(a.isalpha()))
print('ele é numerico? {}' .format(a.isnumeric()))
print('ele é alfanumerico? {}' .format(a.isalnum()))
print('ele é apenas espaço? {}' .format(a.isspace()))
print('ele é um identicador valido? {}' .format(a.isidentifier()))
print('ele contem apenas digitos numericos? {}' .format(a.isdigit()))
print('ele serve como capitalisado? {}' .format(a.istitle()))
print('ele é imprimivel? {}' .format(a.isprintable()))
print('ele tem só letras maisculas ou só minusculas ? {} e {}' .format(a.isupper(),a.islower()))