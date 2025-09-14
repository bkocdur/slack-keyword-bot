from config import OAUTH_CONFIG, SCOPES
import webbrowser
import urllib.parse
import requests
import json

def main():
    # Manually construct the authorization URL
    redirect_uri = OAUTH_CONFIG["redirect_uris"][0]
    auth_params = {
        'response_type': 'code',
        'client_id': OAUTH_CONFIG["client_id"],
        'redirect_uri': redirect_uri,
        'scope': ' '.join(SCOPES),
        'access_type': 'offline',
        'prompt': 'consent'
    }
    
    auth_url = f"{OAUTH_CONFIG['auth_uri']}?{urllib.parse.urlencode(auth_params)}"
    
    print("Please visit this URL to authorize the application:")
    print(auth_url)
    print(f"\nAfter authorization, you'll be redirected to {redirect_uri}")
    print("Copy the 'code' parameter from the URL and paste it below.")
    
    # Open the browser
    webbrowser.open(auth_url)
    
    # Get the authorization code from user
    auth_code = input("\nEnter the authorization code: ")
    
    # Exchange the code for tokens using direct HTTP request
    token_data = {
        'code': auth_code,
        'client_id': OAUTH_CONFIG["client_id"],
        'client_secret': OAUTH_CONFIG["client_secret"],
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    response = requests.post(OAUTH_CONFIG["token_uri"], data=token_data)
    token_response = response.json()
    
    if 'error' in token_response:
        print(f"Error: {token_response['error']}")
        print(f"Description: {token_response.get('error_description', 'No description')}")
        return
    
    print("\nACCESS TOKEN:", token_response.get('access_token'))
    print("REFRESH TOKEN:", token_response.get('refresh_token'))
    print("\nToken expires in:", token_response.get('expires_in'), "seconds")

if __name__ == "__main__":
    main()
