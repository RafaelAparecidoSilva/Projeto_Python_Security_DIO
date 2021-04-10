import hashlib


arquivo1 = 'comparador_hash1.txt'
arquivo2 = 'comparador_hash2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('Arquivo são diferentes')
    print(f'Hash Arquivo 1: {hash1.hexdigest()}')
    print(f'Hash Arquivo 2: {hash2.hexdigest()}')
else:
    print('Arquivos são iguais')
    print(f'Hash Arquivo 1: {hash1.hexdigest()}')
    print(f'Hash Arquivo 2: {hash2.hexdigest()}')