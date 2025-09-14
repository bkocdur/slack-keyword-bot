# Slack Keyword Research App

A Slack bot that provides Google Ads keyword research functionality directly in your Slack workspace.

## Features

- 🔍 **Keyword Research**: Get search volume, competition level, and monthly trends
- 💬 **Multiple Interfaces**: 
  - Mention the bot: `@keyword-research-bot digital marketing`
  - Slash command: `/keyword-research digital marketing`
  - Direct message the bot
- 📊 **Rich Data**: Monthly search volume breakdown, competition analysis
- ⚡ **Fast Response**: Asynchronous processing to avoid timeouts

## Quick Start

1. **Run the setup script:**
   ```bash
   python setup_slack_app.py
   ```

2. **Create a Slack App:**
   - Go to https://api.slack.com/apps
   - Create new app from scratch
   - Follow the setup instructions printed by the script

3. **Configure your .env file:**
   ```bash
   SLACK_BOT_TOKEN=xoxb-your-actual-token
   SLACK_SIGNING_SECRET=your-signing-secret
   SLACK_VERIFICATION_TOKEN=your-verification-token
   PORT=5000
   ```

4. **Install additional requirements:**
   ```bash
   pip install -r requirements_slack.txt
   ```

5. **Run the app:**
   ```bash
   python slack_app.py
   ```

## Deployment

### Heroku Deployment

1. **Create a Procfile:**
   ```
   web: gunicorn slack_app:app
   ```

2. **Deploy:**
   ```bash
   git add .
   git commit -m "Add Slack app"
   git push heroku main
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set SLACK_BOT_TOKEN=xoxb-your-token
   heroku config:set SLACK_SIGNING_SECRET=your-secret
   heroku config:set SLACK_VERIFICATION_TOKEN=your-token
   ```

### Railway Deployment

1. **Connect your GitHub repository**
2. **Set environment variables in Railway dashboard**
3. **Deploy automatically**

## Slack App Configuration

### Required Bot Token Scopes
- `app_mentions:read` - Listen for @mentions
- `chat:write` - Send messages
- `commands` - Handle slash commands
- `im:read` - Read direct messages
- `im:write` - Send direct messages

### Event Subscriptions
- **Request URL**: `https://your-domain.com/slack/events`
- **Bot Events**:
  - `app_mention`
  - `message.im`

### Slash Commands
- **Command**: `/keyword-research`
- **Request URL**: `https://your-domain.com/slack/command`
- **Description**: Research keyword search volume

## Usage Examples

### Mention the Bot
```
@keyword-research-bot digital marketing
```

### Slash Command
```
/keyword-research seo services
```

### Direct Message
Just send a keyword to the bot in a direct message.

## Response Format

The bot will respond with:
- 📊 Average monthly searches
- 🏆 Competition level (LOW/MEDIUM/HIGH)
- 📅 Monthly search volume breakdown

## Error Handling

The app includes comprehensive error handling:
- Invalid keywords
- API rate limits
- Network timeouts
- Authentication errors

## Development

### Local Testing

1. **Install ngrok for local testing:**
   ```bash
   npm install -g ngrok
   ngrok http 5000
   ```

2. **Use the ngrok URL in your Slack app configuration**

3. **Run the app locally:**
   ```bash
   python slack_app.py
   ```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SLACK_BOT_TOKEN` | Bot User OAuth Token | Yes |
| `SLACK_SIGNING_SECRET` | Signing Secret from app settings | Yes |
| `SLACK_VERIFICATION_TOKEN` | Verification Token | Yes |
| `PORT` | Server port (default: 5000) | No |

## Troubleshooting

### Common Issues

1. **"Invalid signature" error:**
   - Check your `SLACK_SIGNING_SECRET`
   - Ensure request URL is correct

2. **"Missing scope" error:**
   - Add required bot token scopes
   - Reinstall the app to your workspace

3. **"Command not found" error:**
   - Check slash command configuration
   - Ensure request URL is accessible

4. **No response from bot:**
   - Check bot token permissions
   - Verify event subscriptions are enabled

### Logs

The app logs all activities. Check your deployment platform's logs for debugging.

## Security

- All Slack requests are verified using the signing secret
- Bot tokens are stored as environment variables
- No sensitive data is logged

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Slack API documentation
3. Check Google Ads API status
