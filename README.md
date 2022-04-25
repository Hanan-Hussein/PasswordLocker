# PasswordLocker
<img width="1440" alt="Screenshot 2022-04-24 at 18 06 08" src="https://user-images.githubusercontent.com/36597096/164985572-a048a162-f351-44b1-88e4-8ffbd82754aa.png">
# Contact-List

Simple Python App that creates new contacts with properties. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

- Python3.9
- unittest (Python test framework)


## Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/Hanan-Hussein/PasswordLocker.git`
- Open terminal command line then navigate to the root folder of the application. `cd PassswordLocker`
- Run `./app.py` 


## Behaviour Driven Development

0. User Login
   - OUTPUT : 
1. Displays Saved Password the User
   - OUTPUT: "Display Saved Credentials"
   - INPUT: "1"
   - OUTPUT: List of the saved credentials 
2. Create New Credentials
   - OUTPUT: "Create a New Credential"
   - INPUT: "2"
   - OUTPUT: Options for the credentials 
3. Password Choice
   - INPUT: "y" 
   - OUTPUT: Auto generates password of a given length
   - INPUT: "n" 
   - OUTPUT: Gives the user a choice of a custom password 
4. Store an Existing Credential
   - INPUT: "3"
   - INPUT:  Input account name and password
   - OUTPUT: Success message
5. Delete a Credential
   - INPUT: "4"
   - INPUT:  Input account name of the account
   - OUTPUT: Success message
 




