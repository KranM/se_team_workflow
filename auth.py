def authenticate(token):
    if token == "valid_oauth_token":
        return "Authenticated via OAuth"
    return "Invalid Token"