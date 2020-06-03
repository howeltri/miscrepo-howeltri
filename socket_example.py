# good resource - https://wiki.python.org/moin/TcpCommunication

def tcp_sock(address, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((address, port))
    message = b'shalom'
    soc.send(message)
    portion = soc.recv(16)
    received = bytearray()
    while portion:
        received.extend(portion)
        portion = soc.recv(16)
    soc.close()
    return received
