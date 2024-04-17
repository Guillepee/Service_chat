import threading
from message_manager import MessageManager

class MessageReceiver(threading.Thread):
    def __init__(self, socket, id, on_new_message=None):
        """
        Initialize a new MessageReceiver thread to handle incoming messages for a given client socket.
        Inherits from threading.Thread to manage message reception in a separate thread.
        """
        super(MessageReceiver, self).__init__()
        self.socket = socket  # Client socket
        self.on_new_message = on_new_message  # Callback for handling new messages
        self.id = id  # Client identifier
        self.manager_message = MessageManager()  # Instance of MessageManager to log messages

    def read_message(self):
        """
        Read a message from the socket according to a specific protocol.
        The first 2 bytes indicate the length of the message, followed by the message itself.
        This method also handles the case where the client disconnects.
        """
        len_as_array = self.socket.recv(2)  # Read the first 2 bytes indicating the message length
        if len(len_as_array) == 0:
            self.client_is_conected = False  # Mark the client as disconnected if no data received
            return

        # Calculate the actual length of the message
        length = 256 * len_as_array[0] + len_as_array[1]
        self.message = self.socket.recv(length)  # Read the full message based on the length
        print(f"Te han escrito el siguiente mensaje: {self.message.decode('utf-8')}")  # Print the message for debugging

        # Call the callback function if defined
        if self.on_new_message is not None:
            self.on_new_message(self.message, self.id)

    def run(self):
        """
        Run method that is called when the thread starts. It continually checks for new messages
        and processes them until the client is connected.
        """
        self.client_is_conected = True  # Assume the client is connected initially

        while self.client_is_conected:
            self.read_message()  # Read a new message
            self.manager_message.save_message(self.message, self.id)  # Save the received message to the log
