from socket import *

def calculate(equation):
    try:
        # 입력된 문자열을 파싱하여 연산 수행
        equation = equation.replace(" ", "")  # 공백 제거
        for op in ('+', '-', '*', '/'):
            if op in equation:
                operands = equation.split(op)
                operand1, operand2 = map(int, operands)
                if op == '+':
                    return str(operand1 + operand2)
                elif op == '-':
                    return str(operand1 - operand2)
                elif op == '*':
                    return str(operand1 * operand2)
                elif op == '/':
                    return f"{operand1 / operand2:.1f}"  # 소수점 아래 한 자리까지
    except Exception as e:
        return "Error"

def main():
    port = 2500
    BUFSIZE = 1024
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print(addr, '에서 연결되었습니다.')
        
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            result = calculate(data.decode())
            conn.send(result.encode())
        
        conn.close()
    sock.close()

if __name__ == "__main__":
    main()
