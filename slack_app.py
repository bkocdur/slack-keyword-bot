#!/usr/bin/env python3
"""
Slack App for Google Ads Keyword Research
This app provides keyword research functionality through Slack commands.
"""

import os
import json
import logging
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from keyword_research import get_keyword_data
import threading
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Slack configuration
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
SLACK_VERIFICATION_TOKEN = os.getenv('SLACK_VERIFICATION_TOKEN')

# Initialize Slack client
slack_client = WebClient(token=SLACK_BOT_TOKEN)

def format_keyword_data(keyword, data):
    """Format keyword research data for Slack display"""
    if not data:
        return f"❌ No data found for keyword: *{keyword}*"
    
    # Create the main message
    message = f"🔍 *Keyword Research Results for: {keyword}*\n\n"
    
    # Basic metrics
    message += f"📊 *Average Monthly Searches:* {data['avg_monthly_searches']:,}\n"
    message += f"🏆 *Competition Level:* {data['competition']}\n\n"
    
    # Monthly breakdown
    if data.get('monthly_breakdown'):
        message += "*📅 Monthly Search Volume Breakdown:*\n"
        for month, searches in data['monthly_breakdown'].items():
            message += f"• {month}: {searches:,}\n"
    
    return message

def get_keyword_data_safe(keyword):
    """Safely get keyword data with error handling"""
    try:
        # Import the keyword research function
        from keyword_research import get_keyword_data
        return get_keyword_data(keyword)
    except Exception as e:
        logger.error(f"Error getting keyword data for '{keyword}': {str(e)}")
        return None

@app.route('/slack/events', methods=['POST'])
def slack_events():
    """Handle Slack events"""
    try:
        data = request.get_json()
        
        # Handle URL verification
        if data.get('type') == 'url_verification':
            return jsonify({'challenge': data.get('challenge')})
        
        # Handle app mentions
        if data.get('type') == 'event_callback':
            event = data.get('event', {})
            
            if event.get('type') == 'app_mention':
                handle_app_mention(event)
            elif event.get('type') == 'message' and event.get('channel_type') == 'im':
                handle_direct_message(event)
        
        return jsonify({'status': 'ok'})
    
    except Exception as e:
        logger.error(f"Error handling Slack event: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

def handle_app_mention(event):
    """Handle @mentions of the bot"""
    try:
        text = event.get('text', '')
        channel = event.get('channel')
        user = event.get('user')
        
        # Extract keyword from mention text
        # Remove bot mention and extract keyword
        keyword = text.replace('<@U0XXXXXXXX>', '').strip()  # Replace with actual bot user ID
        
        if not keyword:
            response = "👋 Hi! I can help you research keywords. Just mention me with a keyword like: `@keyword-research-bot digital marketing`"
        else:
            # Send initial response
            slack_client.chat_postMessage(
                channel=channel,
                text=f"🔍 Researching keyword: *{keyword}*... This may take a few seconds."
            )
            
            # Get keyword data in a separate thread to avoid timeout
            def research_keyword():
                try:
                    data = get_keyword_data_safe(keyword)
                    message = format_keyword_data(keyword, data)
                    
                    slack_client.chat_postMessage(
                        channel=channel,
                        text=message
                    )
                except Exception as e:
                    slack_client.chat_postMessage(
                        channel=channel,
                        text=f"❌ Error researching keyword '{keyword}': {str(e)}"
                    )
            
            # Run in background thread
            thread = threading.Thread(target=research_keyword)
            thread.start()
    
    except SlackApiError as e:
        logger.error(f"Slack API error: {e.response['error']}")
    except Exception as e:
        logger.error(f"Error handling app mention: {str(e)}")

def handle_direct_message(event):
    """Handle direct messages to the bot"""
    try:
        text = event.get('text', '')
        channel = event.get('channel')
        
        if not text:
            response = "👋 Hi! I can help you research keywords. Just send me a keyword and I'll research it for you!"
        else:
            # Send initial response
            slack_client.chat_postMessage(
                channel=channel,
                text=f"🔍 Researching keyword: *{text}*... This may take a few seconds."
            )
            
            # Get keyword data in a separate thread
            def research_keyword():
                try:
                    data = get_keyword_data_safe(text)
                    message = format_keyword_data(text, data)
                    
                    slack_client.chat_postMessage(
                        channel=channel,
                        text=message
                    )
                except Exception as e:
                    slack_client.chat_postMessage(
                        channel=channel,
                        text=f"❌ Error researching keyword '{text}': {str(e)}"
                    )
            
            # Run in background thread
            thread = threading.Thread(target=research_keyword)
            thread.start()
    
    except SlackApiError as e:
        logger.error(f"Slack API error: {e.response['error']}")
    except Exception as e:
        logger.error(f"Error handling direct message: {str(e)}")

@app.route('/slack/command', methods=['POST'])
def slack_command():
    """Handle slash commands"""
    try:
        data = request.form
        command = data.get('command')
        text = data.get('text', '').strip()
        channel_id = data.get('channel_id')
        user_id = data.get('user_id')
        
        if command == '/keyword-research':
            if not text:
                return jsonify({
                    'response_type': 'ephemeral',
                    'text': 'Please provide a keyword to research. Usage: `/keyword-research digital marketing`'
                })
            
            # Send initial response
            slack_client.chat_postMessage(
                channel=channel_id,
                text=f"🔍 Researching keyword: *{text}*... This may take a few seconds."
            )
            
            # Get keyword data in a separate thread
            def research_keyword():
                try:
                    data = get_keyword_data_safe(text)
                    message = format_keyword_data(text, data)
                    
                    slack_client.chat_postMessage(
                        channel=channel_id,
                        text=message
                    )
                except Exception as e:
                    slack_client.chat_postMessage(
                        channel=channel_id,
                        text=f"❌ Error researching keyword '{text}': {str(e)}"
                    )
            
            # Run in background thread
            thread = threading.Thread(target=research_keyword)
            thread.start()
            
            return jsonify({
                'response_type': 'ephemeral',
                'text': 'Keyword research started! Results will appear shortly.'
            })
        
        return jsonify({'text': 'Unknown command'})
    
    except Exception as e:
        logger.error(f"Error handling slash command: {str(e)}")
        return jsonify({'text': 'Error processing command'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'keyword-research-slack-app'})

if __name__ == '__main__':
    # Validate required environment variables
    required_vars = ['SLACK_BOT_TOKEN', 'SLACK_SIGNING_SECRET']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {missing_vars}")
        exit(1)
    
    # Start the Flask app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
