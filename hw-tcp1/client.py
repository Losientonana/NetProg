import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

name = "JeonHaYoon"
sock.send(name.encode())

student_id_bytes = sock.recv(1024)
student_id = int.from_bytes(student_id_bytes, 'big')
print(student_id)
sock.close()