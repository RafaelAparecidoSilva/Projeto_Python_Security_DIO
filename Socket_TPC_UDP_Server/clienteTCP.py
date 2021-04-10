import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print('A conexão falhou!')
        print(f'Erro: {erro}')
        sys.exit()

    print('Socket criado com sucesso!')
    host_alvo = input('Digite o Host ou IP a ser conectado: ')
    porta_alvo = int(input('Digite a porta a ser conectada: '))

    try:
        s.connect((host_alvo, porta_alvo))
        print(f'Cliente TCP conectado com sucesso no host ({host_alvo}) e na porta ({porta_alvo})')
        s.shutdown(2)
    except socket.error as err:
        print(f'Não foi possível se conectar no Host ({host_alvo}), porta ({porta_alvo})')
        print(f'Erro: {err}')
        sys.exit()


if __name__ == '__main__':
    main()
