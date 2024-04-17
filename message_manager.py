import json
import datetime

class MessageManager():
    def __init__(self):
        """
        Initialize the MessageManager instance by loading existing messages from the database.
        It sets up an in-memory list to store message logs that are synced with a JSON file.
        """
        self.log_messages = []  # List to store message logs in memory
        self.load_messages()  # Load messages from the JSON database

    def save_message(self, message, cliente):
        """
        Save a new message to the log and write it to the JSON file. This method formats the message
        data into a dictionary, appends it to the in-memory log list, and then dumps the entire list
        back into the JSON file.
        """
        message_parts = {
            "client": cliente,
            "hour": datetime.datetime.now().isoformat(),  # Format current time to ISO format for JSON compatibility
            "message": message.decode("utf-8")  # Decode the message from bytes to a UTF-8 string
        }

        self.load_messages()  # Reload messages to ensure the list is up-to-date
        self.log_messages.append(message_parts)  # Append the new message to the list

        with open("db_messages.json", "w") as jsonfile:
            json.dump(self.log_messages, jsonfile, indent=4)  # Write the updated list back to the file with indentation for readability

    def load_messages(self):
        """
        Load messages from the JSON file into the in-memory list. This method reads the file and
        updates the list of messages, ensuring that any changes in the file are reflected in the application.
        """
        with open("db_messages.json") as jsonfile:
            self.log_messages = json.load(jsonfile)  # Load messages from file and assign them to the log list
