"""
Configuration file for Google Ads Keyword Research Tool
Uses environment variables for sensitive credentials
"""

import os

# Google Ads Configuration
CUSTOMER_ID = os.getenv("GOOGLE_ADS_CUSTOMER_ID", "1640547396")

# Default keyword to research
DEFAULT_KEYWORD = "digital marketing dubai"

# Google Ads API Configuration
# Uses environment variables for sensitive data
GOOGLE_ADS_CONFIG = {
    "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
    "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
    "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
    "use_proto_plus": True
}

# OAuth2 Configuration for refresh token generation
OAUTH_CONFIG = {
    "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
    "redirect_uris": ["http://127.0.0.1:8000/search-terms/oauth2callback"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
}

# API Settings
LANGUAGE_CODE = "languageConstants/1000"  # English
LOCATION_CODE = "geoTargetConstants/784"  # United Arab Emirates
NETWORK_TYPE = "GOOGLE_SEARCH"
SCOPES = ["https://www.googleapis.com/auth/adwords"]
