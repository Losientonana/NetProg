from socket import *
import base64

def process_request(req):
    req_line = req[0]
    target_file = req_line.split()[1][1:]
    if target_file != 'index.html':
        error_response = 'HTTP/1.1 404 Not Found\r\n\r\n<html><title>Not Found</title><body>Not Found</body></html>'.encode()
        return error_response
    
    try:
        if target_file == "index.html":
            content_type = 'text/html'
            iot_image_encoded = base64.b64encode(open('iot.png', 'rb').read()).decode()
            favicon_encoded = base64.b64encode(open('favicon.ico', 'rb').read()).decode()

            html_content = f'''
                <html>
                <head>
                    <title>My Web Server</title>
                    <link rel="icon" href="data:image/x-icon;base64,{favicon_encoded}">
                </head>
                <body>
                    <h1사물인터넷학과에 홈페이지 오신것을 환영합니다</h1>
                    <p>저는 사물인터넷학과 19학번 전하윤입니다.</p>
                    <div>
                        <img src="data:image/png;base64,{iot_image_encoded}">
                        <p> 사물인터넷학과 캐릭터 </p>
                    </div>
                </body>
                </html>
            '''.encode('euc-kr')

            header_content = f'HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n'.encode()
            full_response = header_content + html_content

    except FileNotFoundError:
        full_response = 'HTTP/1.1 404 Not Found\r\n\r\n<html><title>Not Found</title><body>Not Found</body></html>'.encode()
    return full_response

web_server_socket = socket(AF_INET, SOCK_STREAM)
web_server_socket.bind(('', 80))
web_server_socket.listen(10)
print('Waiting for clients')

while True:
    conn, address = web_server_socket.accept()
    print(f'Connection from {address}')
    received_data = conn.recv(1025)
    
    if not received_data:
        break

    
    decoded_data = received_data.decode()
    request_lines = decoded_data.split("\r\n")
    response_content = process_request(request_lines)
    conn.send(response_content)
    conn.close()
