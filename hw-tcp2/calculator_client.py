from socket import *

def main():
    port = 2500
    BUFSIZE = 1024
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', port))
    
    while True:
        equation = input("계산식을 입력하세요 (예: 20 + 17), 종료하려면 q를 입력: ")
        if equation == 'q':
            break
        sock.send(equation.encode())
        
        result = sock.recv(BUFSIZE)
        print("결과:", result.decode())
    
    sock.close()

if __name__ == "__main__":
    main()
