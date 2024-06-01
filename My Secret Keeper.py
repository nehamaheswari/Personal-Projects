from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file
        self.data_file = data_file
        self.key = None
        self.passwords = {}

        if not os.path.exists(self.key_file):
            self._generate_key()
        self.key = Fernet(self._read_key(self.key_file))

        if not os.path.exists(self.data_file):
            self.save_data()

    def _generate_key(self):
        with open(self.key_file, 'wb') as f:
            f.write(self.key.generate_key())

    def _read_key(self, file):
        with open(file, 'rb') as f:
            return f.read()

    def _decrypt_data(self, data):
        return self.key.decrypt(data)

    def _encrypt_data(self, data):
        return self.key.encrypt(data)

    def _load_data(self):
        with open(self.data_file, 'rb') as f:
            data = f.read()

        if data:
            return json.loads(self._decrypt_data(data))

        return {}

    def save_data(self):
        with open(self.data_file, 'wb') as f:
            f.write(self._encrypt_data(json.dumps(self.passwords).encode()))

    def add_password(self, website, username, password):
        self.passwords[website] = {'username': username, 'password': password}
        self.save_data()

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]

        return None

if __name__ == "__main__":
    manager = PasswordManager()

    while True:
        print("\nPassword Manager:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_password(website, username, password)
            print("Password added successfully!")
        elif choice == '2':
            website = input("Enter website: ")
            data = manager.get_password(website)
            if data:
                print(f"Username: {data['username']}")
                print(f"Password: {data['password']}")
            else:
                print("Password not found!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")