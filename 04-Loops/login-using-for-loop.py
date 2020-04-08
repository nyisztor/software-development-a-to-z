def login(username: str, password: str) -> bool:
    is_authenticated = False

    if username == "admin" and password == "1234":
        is_authenticated = True
    
    return is_authenticated

user = input("Username: ")
passw = input("Password: ")

is_authenticated = False

for attempt in range(4):
    if login(user, passw) == True:
        is_authenticated = True
        break
    else: 
        print("Login failed, re-enter your credentials.")
        user = input("Username: ")
        passw = input("Password: ")

print("Login successful." if is_authenticated else "Your account has been temporarily locked.")