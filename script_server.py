import socket
from message_manager import MessageManager
from chat_thread import MessageReceiver

class Server():
    def __init__(self):
        """
        Initialize the server instance, setting up a list to keep track of connected clients
        and initializing the message manager to handle the distribution of messages.
        """
        self.clients = []  # List to keep track of connected clients
        self.messange_manager = MessageManager()  # Instantiate the message manager

    def send_message(self, message, client_port):
        """
        Send a message to all connected clients except the sender. This method iterates through
        all clients and sends the message to each client whose port number does not match
        the sender's port number.
        """
        for client in self.clients:
            if client_port != client.getpeername()[1]:  # Avoid sending message back to the sender
                client.sendall(len(message).to_bytes(2, byteorder='big'))  # Send message length first
                client.sendall(message)  # Send the actual message

    def run(self):
        """
        Run the server, setting up a socket to listen for incoming connections and handling
        each connection by starting a new thread to receive messages. The server remains open
        to accept multiple clients and manages their connections concurrently.
        """
        acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create server socket
        acceptor.bind(("0.0.0.0", 8080))  # Bind the socket to localhost on port 8080
        acceptor.listen(2)  # Allow up to 2 clients to queue for connections
        print("Servidor Abierto - A la espera de clientes...")  # Inform that the server is ready and waiting

        # First client connection handling
        conn, address = acceptor.accept()  # Accept the first connection
        self.clients.append(conn)  # Add the connected client to the list
        print(f"Cliente {address[1]} se ha conectado")  # Log the connection

        receiver_thread = MessageReceiver(conn, address[1], self.send_message)  # Create a receiver thread for the client
        receiver_thread.start()  # Start the receiver thread

        # Second client connection handling
        conn2, address2 = acceptor.accept()  # Accept the second connection
        self.clients.append(conn2)  # Add the second client to the list
        print(f"Cliente {address2[1]} se ha conectado")  # Log the second connection

        receiver_thread2 = MessageReceiver(conn2, address2[1], self.send_message)  # Same for the second client
        receiver_thread2.start()  # Start the second receiver thread

        acceptor.close()  # Close the server socket after accepting clients
        receiver_thread.join()  # Wait for the first thread to complete
        receiver_thread2.join()  # Wait for the second thread to complete

# Create an instance of Server
server = Server()

if __name__ == "__main__":
    server.run()  # Run the server if the script is the main program
