# Import necessary libraries
from datetime import datetime

# Define a dummy data model
class User:
    """
    A dummy User model for demonstration purposes.
    """

    def __init__(self, user_id, username, email, created_at=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_at = created_at or datetime.utcnow()

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.email}, {self.created_at})"

    def to_dict(self):
        """
        Convert the user object to a dictionary.
        """
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
        }

    def save(self):
        """
        Dummy save method to simulate saving to a database.
        """
        print(f"Saving user {self.username} to the database...")

    @staticmethod
    def get_by_id(user_id):
        """
        Dummy static method to simulate fetching a user by ID.
        """
        print(f"Fetching user with ID {user_id} from the database...")
        # Return a dummy user object
        return User(user_id, "dummy_user", "dummy_email@example.com")


# Example usage
if __name__ == "__main__":
    # Create a new user
    user = User(1, "johndoe", "johndoe@example.com")

    # Display user details
    print(user)

    # Convert to dictionary
    print(user.to_dict())

    # Save the user
    user.save()

    # Fetch a user by ID
    fetched_user = User.get_by_id(1)
    print(f"user: {fetched_user}")
