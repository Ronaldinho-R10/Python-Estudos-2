import socket

target_host='www.google.com'
target_port=80

#Criando um objeto do tipo socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Criando Conexão com o cliente
client.connect((target_host,target_port))
#Enviando dados
client.send(b"GET / HTTP/1.1/r/nHost: www.google.com\r\n\r\n")
#Recebendo dados
response=client.recv(4096)
print(response)



