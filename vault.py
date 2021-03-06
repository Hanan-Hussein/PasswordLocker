from password_generator import PasswordGenerator


class Credentials:
    """
    Creates credentials account which takes account name,
    username, password and saves them in a vault.
    """
    password_vault = {}

    def __init__(self, account_name, password, username):
        """
        initialize credentials

        Args:
            account_name (str): account name
            password (str): takes account password
            username (str): username used in the account
        """
        self.account_name = account_name
        self.password = password
        self.username = username
        Credentials.password_vault[account_name] = {username: password}

    @classmethod
    def delete_credential(cls, account_name):
        """
        Deletes a user by account name

        Args:
            account_name (str): The name of the account to be deleted

        Returns:
            str: account name or the fail report
        """
        return cls.password_vault.pop(account_name, "The account does not exist")

    @classmethod
    def display_credentials(cls):
        """
        Display all the credentials the user has access to

        Returns:
            dict: a collection of all the credentials the user has access to
        """
        return cls.password_vault

    @staticmethod
    def auto_generate_password(length):
        """
            Generates a new password using the auto generator
        Args:
            length (int): length of the password
        """
        return PasswordGenerator().non_duplicate_password(length)


class User:
    """
    creates a new user, and authenticates a user to the system
    """
    local_credentials = ()

    def __init__(self, local_username, local_password):
        """initialize user

        Args:
            password (str): user password 
            username (str): username of the user
        """
        self.local_username = local_username
        self.local_password = local_password
        User.local_credentials = (local_username, local_password)

    @classmethod
    def authenticate(cls, username, password):
        """Authenticate user into the system

        Args:
            username (str): username to authenticate
            password (str): password to authenticate
        """
        if (username, password) == cls.local_credentials:
            return True
        return False
