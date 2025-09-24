#checks if a certain user name is greater or less than 10
username = input("Enter Username: ")

if(len(username) > 10): 
    print("This username has greater than 10 characters", len(username))

else: 
    print("This username has less than 10 characters", len(username))