def authenticate(username, password):
    if username == "admin" and password == "secret":
        return "Login Successful"
    return "Login Failed"