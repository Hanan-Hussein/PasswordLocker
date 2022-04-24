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

