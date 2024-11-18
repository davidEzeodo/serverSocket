import socket


def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET tells the computer that you want it ti use the
    # IPv4 address family. While the SOCK_STREAM is a setting in Net.prog. that tells the computer you want to use
    # TCP for communication.
    # There is also an option for specifying a UDP socket: socket.SOCKET_DGRAM
    # In case you want to go more low-level, than that and build your own transport layer protocol on top of TCP/IP
    # you can use socket.RAW_SOCKET.

    server_ip = "127.0.0.1"
    server_port = 8080
    sock.bind((server_ip, server_port))
    sock.listen(0)
    print(f"Listening on {server_ip}: {server_port}")

    client_socket, client_address = sock.accept()
    print(f"Accept connection from {client_address[0]}:{client_address[1]}")

    while True:

        request = client_socket.recv(1024)
        request = request.decode("utf-8")  # converts bytes to string

        # if we receive "close" from the client, then we break
        # out of the loop and close the connection
        if request.lower() == "close":
            # send response to the client which acknowledges that
            # connection should be closed and break out of the loop
            client_socket.send("closed".encode("utf-8"))
            break
        print(f"Received: {request}")


if __name__ == '__main__':
    run_server()
