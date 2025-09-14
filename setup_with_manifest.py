#!/usr/bin/env python3
"""
Setup script for Slack Keyword Research App using Manifest
This is the EASIEST way to set up your Slack app!
"""

import os
import sys
import json
import subprocess

def print_manifest_instructions():
    """Print instructions for using the manifest"""
    print("\n" + "="*70)
    print("🚀 EASIEST WAY TO CREATE YOUR SLACK APP")
    print("="*70)
    print("\n📋 STEP-BY-STEP INSTRUCTIONS:")
    print("\n1. Go to https://api.slack.com/apps")
    print("2. Click 'Create New App'")
    print("3. Choose 'From an app manifest'")
    print("4. Select your workspace")
    print("5. Copy and paste the manifest from 'slack_app_manifest.json':")
    print("\n" + "-"*50)
    
    # Read and display the manifest
    try:
        with open('slack_app_manifest.json', 'r') as f:
            manifest = json.load(f)
        print(json.dumps(manifest, indent=2))
    except Exception as e:
        print(f"Error reading manifest: {e}")
    
    print("\n" + "-"*50)
    print("\n6. Click 'Next' and then 'Create'")
    print("7. Go to 'Install App' and click 'Install to Workspace'")
    print("8. Copy the 'Bot User OAuth Token' (starts with xoxb-)")
    print("9. Go to 'Basic Information' and copy the 'Signing Secret'")
    print("10. Update your .env file with these credentials")
    print("\n" + "="*70)

def create_env_template():
    """Create a template .env file"""
    env_content = """# Slack App Configuration (from manifest setup)
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_SIGNING_SECRET=your-signing-secret-here
SLACK_VERIFICATION_TOKEN=your-verification-token-here

# Server Configuration
PORT=5000
FLASK_ENV=production

# Note: Your Google Ads credentials are already in config.py
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env template file")

def test_manifest():
    """Test that the manifest is valid JSON"""
    try:
        with open('slack_app_manifest.json', 'r') as f:
            manifest = json.load(f)
        print("✅ Manifest file is valid JSON")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in manifest: {e}")
        return False
    except FileNotFoundError:
        print("❌ Manifest file not found")
        return False

def main():
    """Main setup function"""
    print("🔧 Setting up Slack Keyword Research App with Manifest")
    print("This is the EASIEST way to create your Slack app!")
    
    # Check if we're in the right directory
    if not os.path.exists("keyword_research.py"):
        print("❌ Please run this script from the keyword-research-app directory")
        sys.exit(1)
    
    # Test manifest
    if not test_manifest():
        sys.exit(1)
    
    # Create .env template
    create_env_template()
    
    # Print instructions
    print_manifest_instructions()
    
    print("\n🎉 That's it! The manifest approach is much simpler than manual setup.")
    print("\n📝 After creating your app:")
    print("1. Update .env with your actual tokens")
    print("2. Deploy your app to a cloud platform")
    print("3. Update the Request URLs in your Slack app settings")
    print("4. Test with: @your-bot digital marketing")

if __name__ == "__main__":
    main()
