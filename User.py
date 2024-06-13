class User:
    def __init__(self, name, email, drivers_license=None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __str__(self):
        return f"{self.name} with driver's licence #: {self.drivers_license}, has succesfully created an account"

user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com", "XYZ123")
user3 = User("Bartholomew Oobleck", "bartholomew@oobleck.edu")
user4 = User("Agent 47", "hitman@ica.org")