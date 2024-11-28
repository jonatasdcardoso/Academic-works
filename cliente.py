import socket

HOST = '127.0.0.1'  
PORT = 60500        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mensagem = input("Digite sua mensagem ou digite 'sair'para a aplicação: ")
        if mensagem == "sair":
            break
        if not mensagem:
            break
        comando = f"TEXTO {mensagem}"
        s.sendall(comando.encode())
        data = s.recv(1024)
        print(data.decode())