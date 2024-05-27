from socket import *
import time

serverIP = 'localhost'  # 서버의 IP 주소를 적절히 설정하세요
port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
addr = (serverIP, port)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg  
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)  
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            # print("타임아웃, 재전송합니다.")
            reTx += 1
            continue
        else:
            break
    
    if reTx > 5:
        print("메시지 전송 실패.")
        break 
