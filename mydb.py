import json  # Import the JSON module to work with JSON files

class Database:

    def add_data(self, name, email, password):
        """
        Adds user data to the database if the email is not already registered.
        """
        with open('db.json', 'r') as rf:
            database = json.load(rf)
        
        if email in database:
            return 0  # Email is already registered
        else:
            # Add user data to the database
            database[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return 1  # Data added successfully
        
    def search_data(self, email, password):
        """
        Searches for user data in the database and checks if the provided password is correct.
        """
        with open('db.json', 'r') as rf:
            database = json.load(rf)
            
        if email in database:
            if database[email][1] == password:
                return 1  # Email and password match
            else:
                return 0  # Password is incorrect
        else: 
            return 0  # Email not found
