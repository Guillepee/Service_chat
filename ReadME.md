# Prueba Tecnica - EnerClic

# **Chat Application**

This project is a basic chat application that allows multiple clients to connect to a server and communicate with each other in real-time. The server handles connections, message forwarding, and maintains a log of all messages exchanged between clients. Each client can send messages that are relayed by the server to all other connected clients.

## **Components**

- **Server**: Manages incoming connections, client communications, and forwards messages to other connected clients.
- **Client**: Connects to the server, sends messages, and receives messages from other clients.
- **Message Manager**: Handles logging of messages to a JSON file for persistence.
- **Message Receiver**: A thread that handles reading and processing messages from the client in real-time.

## **Setup and Running**

### **Requirements**

- Python 3.6 or higher
- **`socket`** library (standard in Python)
- **`threading`** library (standard in Python)
- **`datetime`** library (standard in Python)
- **`json`** library (standard in Python)

### **Starting the Server**

To start the server, run the **`server.py`** script:

```bash

python server.py
```

This will initialize the server and wait for client connections on localhost port 8080.

### **Running a Client**

To start a client instance, run the **`client.py`** script:

```bash

python client.py
```

Each client will connect to the server on the same localhost and port 8080.

## **Architecture**

The application uses a multi-threaded server to handle real-time communication between multiple clients. The server listens for new connections and starts a new thread (**`MessageReceiver`**) for each connected client to handle incoming messages. The **`MessageManager`** is used to log all messages to a JSON file, providing a simple persistence mechanism.

## **Usage**

Clients can send messages to each other through the command-line interface. When a client sends a message, it is received by the server, which then forwards it to all other connected clients. Messages are logged by the server using the **`MessageManager`**. The application supports basic text-based messaging.

## **Features**

- Real-time messaging between multiple clients.
- Server-managed client connections and message forwarding.
- Persistent message logging.

##