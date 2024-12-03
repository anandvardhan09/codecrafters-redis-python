import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.accept() # wait for client
    comm, tt = server_socket.accept()  # wait for client

    comm, _ = server_socket.accept()  # wait for client

    # Read the incoming data (ignoring the input)
    comm.recv(1024)  # Read data from the client (minimal read, we can ignore the content)

    # Send the response to the client
    comm.sendall(b"+PONG\r\n")
    comm.close()  # Close the connection after responding




if __name__ == "__main__":
    main()
