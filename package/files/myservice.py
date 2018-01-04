import sys
import socket

if __name__ == "__main__":
  tcp_interface = ''
  tcp_port = sys.argv[1]
  listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  listen_socket.bind(tcp_interface, tcp_port)
  listen_socket.listen(1)
  conn, addr = listen_scoket.accept()
  print 'Connected by', addr
  while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
