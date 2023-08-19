import socket
import threading

# Função para lidar com a troca de mensagens de um cliente
def handle_client(client_socket, client_address, clients):
    # Adiciona o cliente à lista de clientes
    clients.append((client_socket, client_address))

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Envia a mensagem para todos os outros clientes
            for other_socket, _ in clients:
                if other_socket != client_socket:
                    try:
                        other_socket.send(f"{client_address[0]}: {message}".encode('utf-8'))
                    except:
                        pass
    except:
        pass

    # Remove o cliente da lista de clientes e fecha o socket
    clients.remove((client_socket, client_address))
    client_socket.close()

# Configurações do servidor
host = '0.0.0.0'
port = 12345

# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta
server_socket.bind((host, port))

# Coloca o socket em modo de escuta
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

# Lista para armazenar os sockets dos clientes
clients = []

# Loop principal para aceitar conexões
while True:
    # Aceita uma nova conexão
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # Inicia uma thread para lidar com o cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
    client_thread.start()