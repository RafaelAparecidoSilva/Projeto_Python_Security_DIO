import hashlib


resultado = hashlib.md5('Python security'.encode('utf-8'))
# resultado = hashlib.md5(b'Python security')
print(resultado)
print(f'O Hash da string é: {resultado.hexdigest()}')
