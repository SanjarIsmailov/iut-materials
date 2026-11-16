import socket

client = socket.socket(socker.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 7070)

while True:
  msg = input("Enter temperature: ")
  client.sendto(msg.encode(), server_addr)

  data, _ = client.recvfrom(1024)
  print("Server: ", data.decode())

  if msg == "/exit"
  break
client.close()
