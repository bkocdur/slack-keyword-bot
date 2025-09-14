#!/usr/bin/env python3
"""
Test script for Slack Keyword Research App
This script tests the app functionality without requiring Slack credentials.
"""

import os
import sys
from keyword_research import get_keyword_data

def test_keyword_research():
    """Test the keyword research functionality"""
    print("🧪 Testing keyword research functionality...")
    
    test_keywords = [
        "digital marketing",
        "seo services", 
        "home cleaning dubai"
    ]
    
    for keyword in test_keywords:
        print(f"\n🔍 Testing keyword: {keyword}")
        try:
            data = get_keyword_data(keyword)
            if data:
                print(f"✅ Success! Found data for '{data['keyword']}'")
                print(f"   📊 Avg monthly searches: {data['avg_monthly_searches']:,}")
                print(f"   🏆 Competition: {data['competition']}")
                if data.get('monthly_breakdown'):
                    print(f"   📅 Monthly data: {len(data['monthly_breakdown'])} months")
            else:
                print(f"❌ No data found for '{keyword}'")
        except Exception as e:
            print(f"❌ Error testing '{keyword}': {str(e)}")

def test_slack_app_imports():
    """Test that all Slack app imports work"""
    print("\n🧪 Testing Slack app imports...")
    
    try:
        from slack_app import format_keyword_data
        print("✅ Slack app imports successful")
        
        # Test formatting function
        test_data = {
            'keyword': 'test keyword',
            'avg_monthly_searches': 10000,
            'competition': 'MEDIUM',
            'monthly_breakdown': {
                'Jan': 8000,
                'Feb': 12000,
                'Mar': 10000
            }
        }
        
        formatted = format_keyword_data('test keyword', test_data)
        print("✅ Formatting function works")
        print(f"📝 Sample formatted output:\n{formatted[:200]}...")
        
    except Exception as e:
        print(f"❌ Error testing Slack app imports: {str(e)}")

def test_environment_setup():
    """Test environment setup"""
    print("\n🧪 Testing environment setup...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file exists")
    else:
        print("⚠️  .env file not found (run setup_slack_app.py first)")
    
    # Check if config.py exists
    if os.path.exists('config.py'):
        print("✅ config.py exists")
    else:
        print("❌ config.py not found")
    
    # Check if slack_app.py exists
    if os.path.exists('slack_app.py'):
        print("✅ slack_app.py exists")
    else:
        print("❌ slack_app.py not found")

def main():
    """Run all tests"""
    print("🚀 Testing Slack Keyword Research App")
    print("=" * 50)
    
    test_environment_setup()
    test_slack_app_imports()
    test_keyword_research()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\n📋 Next steps:")
    print("1. Create a Slack app at https://api.slack.com/apps")
    print("2. Configure the app with the required permissions")
    print("3. Update your .env file with Slack credentials")
    print("4. Deploy the app to a cloud platform")
    print("5. Test with your Slack workspace")

if __name__ == "__main__":
    main()
