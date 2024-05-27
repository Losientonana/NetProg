import socket
import threading

def receive_message(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if msg:
                print(msg.decode())
            else:
                break
        except:
            print("연결이 종료되었습니다.")
            break

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.sendall(('['+my_id+']').encode())

th = threading.Thread(target=receive_message, args=(sock,))
th.daemon = True
th.start()

try:
    while True:
        msg = '[' + my_id + '] ' + input()
        if msg:
            sock.sendall(msg.encode())
        else:
            break
except:
    print("서버 연결이 종료되었습니다.")

sock.close()
