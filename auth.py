def authenticate(username=None, password=None, token=None):
    if token == "valid_oauth_token":
        return "Authenticated via OAuth"
    
    elif username == "admin" and password == "secret":
        return "Login Successful"
        
    return "Authentication Failed"