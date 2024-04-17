import socket
from chat_thread import MessageReceiver
from message_manager import MessageManager

class Client():
    def __init__(self):
        """
        Initialize a new client instance, creating a new socket and connecting to the server.
        This sets up the client to communicate over a specified port.
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a client socket
        self.client.connect(("localhost", 8080))  # Connect to the server at localhost on port 8080
        print("Conexion exitosa con el Servidor en puerto 8080")  # Inform user of successful connection
        self.client_number = self.client.getsockname()[1]  # Retrieve and store the client's port number for reference
        self.message_manager = MessageManager()  # Instantiate the message manager to handle messages

    def get_message(self):
        """
        Start the message handling process for the client. This function creates a new thread
        to receive messages asynchronously and handles sending messages from the user.
        It continues to run until the user sends a termination command.
        """
        self.message_receiver = MessageReceiver(self.client, self.client_number)
        self.message_receiver.start()  # Start the asynchronous message receiver thread

        self.farewell = f"El cliente {self.client_number} se ha descontado del chat"  # Set up a farewell message

        while True:  # Loop to send messages
            message = input("")  # Read user input
            message_encode = message.encode("utf-8")  # Encode the message to UTF-8 for network transmission
            self.client.sendall(len(message_encode).to_bytes(2, byteorder='big'))  # Send the length of the message first
            self.client.sendall(message_encode)  # Send the actual message
            
            if message in ["cerrar", "chau", "adios"]:  # Check for exit commands
                self.client.sendall(self.farewell.encode("utf-8"))  # Send the farewell message
                break  # Exit the message sending loop
        self.message_receiver.join()  # Wait for the receiver thread to finish

if __name__ == "__main__":
    new_client = Client()
    new_client.get_message()  # Start the client's message handling function
