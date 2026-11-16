import socket

server = socket.socker(socker.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 7070))
print("Server is running..")

while True:
  data, addr = server.recvfrom(1024)
  msg = data.decode().strip()

  if msg == "/exit":
    server.sendto("Goodbye!".encode(), addr)
    break
  try:
    temp = float(msg)
    if temp < 10:
      result = "Very cold"
    elif temp < 25:
      result = "Normal"
    elif temp < 35:
      result = "Warm"
    elif temp < 45:
      result = "High temperature"
    else:
      result = "Critical"
  except ValueError:
    result = "Invalid input!, Enter a number"

    server.sendto(result.encode(), addr)
  server.close()
