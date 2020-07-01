import os

welcome_message = '''
Welcome!
NEW - Create a new user
LOGIN - Log in to an existing account
DELETE - Delete an account'''
print(welcome_message)
welcome = input("> ").lower()


class Login:
    def new_user(self):
        while True:
            print("Creating New User... ")
            user = input("Username\n> ")
            password = input("Password\n> ")
            password1 = input("Confirm Password\n> ")
            if password == password1:
                print("Account Created Successfully!")
                file = open(user+".txt", "w")
                file.write(user+":"+password)
                file.close()
                break
            print("Passwords don't match!")

    def returning_user(self):
        while True:
            print("Logging in... ")
            user = input("Username\n> ")
            password = input("Password\n> ")
            file = open(user+".txt", "r")
            data = file.readline()
            file.close()
            if data == user+":"+password:
                print("Welcome")
                break
            print("Incorrect Username/Password... Try Again")

    def remove_user(self):
        while True:
            print("You are about to delete a user... This cannot be undone")
            user = input("Username\n> ")
            password = input("Password\n> ")
            file = open(user+".txt", "r")
            data = file.readline()
            file.close()
            if data == user+":"+password:
                os.remove(f"{user}.txt")
                print("User Deleted Successfully")
                break
            else:
                print("Invalid Credentials, Quitting...")
                break


while True:
    if "new" in welcome:
        Login.new_user(None)
        break
    elif "login" in welcome:
        Login.returning_user(None)
        break
    elif "delete" in welcome:
        Login.remove_user(None)
        break
    else:
        print("Invalid Input... Try Again!")
        break
