from cmd import PROMPT
from vault import User, Credentials
from getpass import getpass
if __name__ == "__main__":

    bannner = "WELCOME TO PASSWORD LOCKER"
    print("\u001b[4m", f"{bannner:^1000}", "\u001b[0m", "\n")
    input("Press enter to create an account with a username and password : ")
    print()
    user_username = input("USERNAME : ")
    print()
    user_password = getpass(prompt="PASSWORD : ")
    print()
    new_user = User(user_username, user_password)
    print("\u001b[32m","ACCOUNT SUCCESSFULLY CREATED","\u001b[0m")    
    print() 
    print("Login to Your Account :")
   
    while True:
        print()
        user_username_verification = input("USERNAME : ")
        print()
        user_password_verification = getpass(prompt="PASSWORD : ")
        print()
        authentification = new_user.authenticate(user_username_verification, user_password_verification)
        if authentification:
            print("\u001b[32m","SUCCESSFUL LOGIN","\u001b[0m")
            print()
            break
        else:
            print("\u001b[31m","WRONG CREDENTIALS\n","\u001b[0m")
        print("TRY AGAIN")
     # Authentified user space
    user_options = {
        "0": "QUIT",
        "1": "Display Saved Credentials",
        "2": "Create New Credentials",
        "3": "Store an existing credentials",
        "4": "Delete a Credential"
    }
    new_credentials_options = {
        "y": "Auto Generated Password",
        "n": "Input Your Custom Password",
        "0": "Quit"
    }
    user_input = None
    main_menu_msg = "Main Menu "
    while user_input != "0":
        # Main Menu
        print(f"{main_menu_msg:^350}")
        for option, message in user_options.items():
            print(f"{option:^30} {message:<30}")
        # Options
        user_input = input(" : ")
        # Display of available credentials
        if user_input == "1":
            account_name, username, password = "ACCOUNT NAME|", "USERNAME|", "PASSWORD|"
            print(f"\t|{account_name:20} |{username:20} |{password:20}")
            for i, j in Credentials.display_credentials().items():
                for k, l in j.items():
                    print()
                    print(f"\t {i:20}  {k:20}  {l}")
            print()
            input("Press Enter To Go Back to Main Menu.....")
            print()