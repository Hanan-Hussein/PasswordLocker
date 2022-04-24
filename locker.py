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
    print("Login to Your Account :")
   
    while True:
        print()
        user_username_verification = input("USERNAME : ")
        print()
        user_password_verification = input("PASSWORD : ")
        print()
        authentification = new_user.authenticate(user_username_verification, user_password_verification)
        if authentification:
            print("\u001b[32m","SUCCESSFULL LOGIN","\u001b[0m")
            print()
            break
        else:
            print("\u001b[31m","WRONG CREDENTIALS\n","\u001b[0m")
        print("TRY AGAIN")
