#!/usr/bin/env python3
"""
Setup script for Slack Keyword Research App
This script helps you set up the Slack app with proper configuration.
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages for Slack app"""
    print("📦 Installing Slack app requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_slack.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_env_file():
    """Create .env file from template"""
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"⚠️  {env_file} already exists. Skipping creation.")
        return True
    
    print(f"📝 Creating {env_file} file...")
    env_content = """# Slack App Configuration
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_SIGNING_SECRET=your-signing-secret-here
SLACK_VERIFICATION_TOKEN=your-verification-token-here

# Server Configuration
PORT=5000
FLASK_ENV=production
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print(f"✅ {env_file} created successfully!")
        print("📋 Please edit .env file with your actual Slack app credentials.")
        return True
    except Exception as e:
        print(f"❌ Error creating {env_file}: {e}")
        return False

def check_config():
    """Check if configuration files exist"""
    print("🔍 Checking configuration...")
    
    required_files = ["config.py", "slack_app.py", "keyword_research.py"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ All required files found!")
    return True

def print_setup_instructions():
    """Print setup instructions"""
    print("\n" + "="*60)
    print("🚀 SLACK APP SETUP INSTRUCTIONS")
    print("="*60)
    print("\n1. Create a Slack App:")
    print("   • Go to https://api.slack.com/apps")
    print("   • Click 'Create New App'")
    print("   • Choose 'From scratch'")
    print("   • Name your app (e.g., 'Keyword Research Bot')")
    print("   • Select your workspace")
    print("\n2. Configure OAuth & Permissions:")
    print("   • Go to 'OAuth & Permissions' in your app settings")
    print("   • Add these Bot Token Scopes:")
    print("     - app_mentions:read")
    print("     - chat:write")
    print("     - commands")
    print("     - im:read")
    print("     - im:write")
    print("   • Install the app to your workspace")
    print("   • Copy the 'Bot User OAuth Token' (starts with xoxb-)")
    print("\n3. Set up Event Subscriptions:")
    print("   • Go to 'Event Subscriptions'")
    print("   • Enable Events: ON")
    print("   • Request URL: https://your-domain.com/slack/events")
    print("   • Subscribe to bot events:")
    print("     - app_mention")
    print("     - message.im")
    print("\n4. Create Slash Commands:")
    print("   • Go to 'Slash Commands'")
    print("   • Create New Command:")
    print("     - Command: /keyword-research")
    print("     - Request URL: https://your-domain.com/slack/command")
    print("     - Short Description: Research keyword search volume")
    print("     - Usage Hint: digital marketing")
    print("\n5. Update your .env file with:")
    print("   • SLACK_BOT_TOKEN (from step 2)")
    print("   • SLACK_SIGNING_SECRET (from Basic Information)")
    print("   • SLACK_VERIFICATION_TOKEN (from Basic Information)")
    print("\n6. Deploy your app:")
    print("   • Deploy to Heroku, Railway, or any cloud platform")
    print("   • Update the Request URLs in Slack with your deployed URL")
    print("\n7. Test your app:")
    print("   • Mention the bot: @your-bot-name digital marketing")
    print("   • Use slash command: /keyword-research digital marketing")
    print("   • Send direct message to the bot")
    print("\n" + "="*60)

def main():
    """Main setup function"""
    print("🔧 Setting up Slack Keyword Research App...")
    
    # Check if we're in the right directory
    if not os.path.exists("keyword_research.py"):
        print("❌ Please run this script from the keyword-research-app directory")
        sys.exit(1)
    
    # Run setup steps
    steps = [
        ("Checking configuration", check_config),
        ("Installing requirements", install_requirements),
        ("Creating environment file", create_env_file),
    ]
    
    for step_name, step_func in steps:
        print(f"\n{step_name}...")
        if not step_func():
            print(f"❌ Setup failed at step: {step_name}")
            sys.exit(1)
    
    print("\n✅ Setup completed successfully!")
    print_setup_instructions()

if __name__ == "__main__":
    main()
