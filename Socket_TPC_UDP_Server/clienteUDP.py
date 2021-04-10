import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket foi criado com sucesso!!!')

host = 'localhost'
porta = 5433
msg = 'Teste no servidor!'

try:
    print('Cliente: ' + msg)
    s.sendto(msg.encode(), (host, 5432))
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Fechando conexão!')
    s.close()
