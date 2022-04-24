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
