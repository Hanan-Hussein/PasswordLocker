from vault import User, Credentials
if __name__ == "__main__":

    bannner = "WELCOME TO PASSWORD LOCKER"
    print("\u001b[4m", f"{bannner:^1000}", "\u001b[0m", "\n")
    input("Press enter to create an account with a username and password : ")
    print()
    user_username = input("USERNAME : ")
    print()
    user_password = input("PASSWORD : ")
    print()
    new_user = User(user_username, user_password)
    print("\u001b[32m","ACCOUNT SUCCESSFULLY CREATED","\u001b[0m")    
    print()
