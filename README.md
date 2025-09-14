# Google Ads Keyword Research Tool

A Python application for conducting keyword research using the Google Ads API.

## Features

- Generate keyword ideas based on seed keywords
- Get monthly search volume data
- Analyze competition levels
- View historical search volume trends

## Prerequisites

1. **Google Ads Account**: You need an active Google Ads account
2. **Google Ads API Access**: Request access to the Google Ads API
3. **Developer Token**: Obtain a developer token from Google Ads
4. **OAuth2 Credentials**: Set up OAuth2 credentials in Google Cloud Console

## Setup Instructions

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Generate Refresh Token

Before running the main application, you need to generate a refresh token:

```bash
python generate_refresh_token.py
```

This will:
- Open your browser for OAuth2 authentication
- Ask for permission to access your Google Ads account
- Display the refresh token in the terminal

### 3. Update Configuration

Edit `keyword_research.py` and replace `INSERT_REFRESH_TOKEN_HERE` with the refresh token you generated in step 2.

### 4. Configure Your Settings

Update the following variables in `keyword_research.py`:

- `CUSTOMER_ID`: Your Google Ads customer ID (digits only, no hyphens)
- `KEYWORD`: The seed keyword you want to research
- `config`: Update with your actual credentials

## Usage

Run the keyword research tool:

```bash
python keyword_research.py
```

## Output

The tool will display:
- Average monthly searches for the keyword
- Competition level (LOW, MEDIUM, HIGH)
- Monthly search volume breakdown (if available)
- Related keyword suggestions if exact match not found

## Troubleshooting

### Common Issues

1. **Authentication Errors**: Make sure your refresh token is valid and not expired
2. **API Access Denied**: Verify your developer token is approved and active
3. **Customer ID Issues**: Ensure the customer ID is correct and you have access to it

### Error Messages

- `GoogleAdsException`: Check your API credentials and permissions
- `Authentication Error`: Regenerate your refresh token
- `Permission Denied`: Verify your Google Ads account has API access

## Security Notes

- Never commit your refresh token or API credentials to version control
- Consider using environment variables for sensitive data
- Regularly rotate your API credentials

## API Limits

Be aware of Google Ads API rate limits and quotas. The free tier has limited requests per day.

## Support

For issues related to:
- Google Ads API: Check the [official documentation](https://developers.google.com/google-ads/api)
- This tool: Review the error messages and configuration
