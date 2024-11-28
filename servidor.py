import socket

HOST = '127.0.0.1'
PORT = 60500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Professor, o servidor está locado em escutando em IP/PORTA {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            mensagem = data.decode()
            if mensagem.startswith("TEXTO"):
                texto = mensagem.split(" ", 1)[1]  
                print(f"O texto recebido pelo cliente foi: {texto}")
                conn.sendall("RECEBIDO: Mensagem recebida com sucesso pelo servidor!".encode())
            else:
                print(f"Recebido: {mensagem}")
                conn.sendall("RECEBIDO: Mensagem recebida com sucesso pelo servidor!".encode())