import os

with open('dados.txt') as file:
    arquivo = file.read().splitlines()
    for ip in arquivo:
        os.system(f'ping {ip}')
        print('-=' * 50)
