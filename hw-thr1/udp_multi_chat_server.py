import socket
import threading
import time

def client_handler(client_sock, addr):
    while True:
        try:
            data = client_sock.recv(1024)
            if data:
                print(time.asctime() + str(addr) + ':' + data.decode())
                # 모든 클라이언트에게 메시지 전송
                for client in clients:
                    if client != client_sock:
                        client.send(data)
            else:
                break
        except:
            break
    print(f"{addr} 연결이 종료되었습니다.")
    client_sock.close()
    clients.remove(client_sock)

def accept_connections(s):
    while True:
        client_sock, addr = s.accept()
        print(f"{addr}에서 새로운 연결이 수립되었습니다.")
        clients.append(client_sock)
        th = threading.Thread(target=client_handler, args=(client_sock,addr))
        th.start()

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2500))
s.listen(5)

print('서버 시작')
accept_connections(s)
