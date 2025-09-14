# Slack App Deployment with Manifest

This is the **EASIEST** way to deploy your Keyword Research Slack Bot!

## 🚀 Quick Start (5 minutes)

### 1. Create Slack App with Manifest
1. Go to https://api.slack.com/apps
2. Click **"Create New App"**
3. Choose **"From an app manifest"**
4. Select your workspace
5. Copy the entire manifest from `slack_app_manifest.json` and paste it
6. Click **"Next"** then **"Create"**

### 2. Install Your App
1. Go to **"Install App"** in your app settings
2. Click **"Install to Workspace"**
3. Copy the **"Bot User OAuth Token"** (starts with `xoxb-`)
4. Go to **"Basic Information"** and copy the **"Signing Secret"**

### 3. Update Environment Variables
Edit your `.env` file:
```bash
SLACK_BOT_TOKEN=xoxb-your-actual-token-here
SLACK_SIGNING_SECRET=your-actual-signing-secret-here
SLACK_VERIFICATION_TOKEN=your-verification-token-here
PORT=5000
FLASK_ENV=production
```

### 4. Deploy to Cloud Platform

#### Option A: Railway (Recommended)
1. Go to https://railway.app
2. Connect your GitHub repository
3. Set environment variables in Railway dashboard
4. Deploy automatically

#### Option B: Heroku
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set SLACK_BOT_TOKEN=xoxb-your-token
   heroku config:set SLACK_SIGNING_SECRET=your-secret
   heroku config:set SLACK_VERIFICATION_TOKEN=your-token
   ```
4. Deploy: `git push heroku main`

#### Option C: Render
1. Go to https://render.com
2. Connect your GitHub repository
3. Set environment variables
4. Deploy

### 5. Update Slack App URLs
After deployment, update these URLs in your Slack app settings:

**Event Subscriptions:**
- Request URL: `https://your-app.railway.app/slack/events`

**Slash Commands:**
- Request URL: `https://your-app.railway.app/slack/command`

### 6. Test Your Bot! 🎉

**Mention the bot:**
```
@Keyword Research Bot digital marketing
```

**Use slash command:**
```
/keyword-research seo services
```

**Send direct message:**
Just send a keyword to the bot in a DM.

## 📋 What the Manifest Does

The manifest automatically configures:
- ✅ Bot user with proper permissions
- ✅ Slash command `/keyword-research`
- ✅ Event subscriptions for mentions and DMs
- ✅ OAuth scopes (no manual setup needed!)
- ✅ App metadata and descriptions

## 🔧 Local Testing

For local testing with ngrok:

1. **Install ngrok:**
   ```bash
   npm install -g ngrok
   ```

2. **Start your app:**
   ```bash
   python slack_app_manifest.py
   ```

3. **Start ngrok:**
   ```bash
   ngrok http 5000
   ```

4. **Use ngrok URL in Slack app settings:**
   - Event Subscriptions: `https://abc123.ngrok.io/slack/events`
   - Slash Commands: `https://abc123.ngrok.io/slack/command`

## 🐛 Troubleshooting

### Common Issues:

1. **"Invalid signature" error:**
   - Check your `SLACK_SIGNING_SECRET`
   - Ensure your app is deployed and accessible

2. **"Missing scope" error:**
   - The manifest should handle this automatically
   - Reinstall the app if needed

3. **Bot not responding:**
   - Check that event subscriptions are enabled
   - Verify the Request URL is correct
   - Check your deployment logs

4. **"Command not found":**
   - Ensure slash command is properly configured
   - Check the Request URL

### Debug Mode:
Set `FLASK_ENV=development` in your `.env` file for detailed logs.

## 🎯 Why Manifest is Better

- ✅ **No manual configuration** - everything is automated
- ✅ **Less error-prone** - no missing permissions or settings
- ✅ **Version controlled** - manifest is in your code
- ✅ **Reproducible** - anyone can recreate the exact same app
- ✅ **Faster setup** - 5 minutes vs 30 minutes

## 📞 Support

If you run into issues:
1. Check the deployment logs
2. Verify environment variables
3. Test the health endpoint: `https://your-app.com/health`
4. Check Slack app settings match your deployment URLs
