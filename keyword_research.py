from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import sys
from config import CUSTOMER_ID, DEFAULT_KEYWORD, GOOGLE_ADS_CONFIG, LANGUAGE_CODE, LOCATION_CODE, NETWORK_TYPE

def get_keyword_data(keyword):
    """
    Get keyword research data for a given keyword.
    Returns a dictionary with keyword metrics or None if error.
    """
    try:
        print(f"🔍 Researching keyword: {keyword}")
        print(f"📍 Location: Global (geo targeting temporarily disabled)")
        print(f"🌐 Language: English (languageConstants/1000)")
        
        client = GoogleAdsClient.load_from_dict(GOOGLE_ADS_CONFIG)

        service = client.get_service("KeywordPlanIdeaService")

        request = client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = CUSTOMER_ID
        request.language = LANGUAGE_CODE
        # Temporarily remove geo targeting to test
        # request.geo_target_constants.append(LOCATION_CODE)
        request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum[NETWORK_TYPE]
        request.keyword_seed.keywords.append(keyword)

        print(f"📡 Making API request...")
        response = service.generate_keyword_ideas(request=request)
        
        # Convert to list to check length
        ideas_list = list(response)
        print(f"📊 Received {len(ideas_list)} keyword ideas")
        
        for idea in ideas_list:
            print(f"🔍 Checking idea: '{idea.text}' (target: '{keyword}')")
            if idea.text.lower() == keyword.lower():
                metrics = idea.keyword_idea_metrics
                print(f"✅ Found exact match! Avg searches: {metrics.avg_monthly_searches}")
                
                # Prepare monthly breakdown data
                monthly_breakdown = {}
                if metrics.monthly_search_volumes:
                    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                    
                    for mv in metrics.monthly_search_volumes:
                        # Handle the special case where 13 = January
                        if mv.month == 13:
                            month_name = "Jan"
                        elif 1 <= mv.month <= 12:
                            month_name = month_names[mv.month - 1]
                        else:
                            month_name = f"Unknown({mv.month})"
                        
                        monthly_breakdown[month_name] = mv.monthly_searches
                
                return {
                    'keyword': idea.text,
                    'avg_monthly_searches': metrics.avg_monthly_searches,
                    'competition': metrics.competition.name,
                    'monthly_breakdown': monthly_breakdown
                }
        
        print(f"❌ No exact match found for '{keyword}'")
        
        # If exact keyword not found, return the first few suggestions
        suggestions = []
        for idea in ideas_list[:5]:
            suggestions.append({
                'keyword': idea.text,
                'avg_monthly_searches': idea.keyword_idea_metrics.avg_monthly_searches
            })
        
        print(f"💡 Found {len(suggestions)} suggestions")
        return {
            'keyword': keyword,
            'exact_match': False,
            'suggestions': suggestions
        }

    except GoogleAdsException as ex:
        print(f"❌ Google Ads API Error:")
        print(f"Request ID: {ex.request_id}")
        print(f"Status: {ex.error.code().name}")
        print(f"Error: {ex.error.message()}")
        error_messages = []
        for error in ex.failure.errors:
            error_messages.append(f"{error.error_code}: {error.message}")
        raise Exception(f"Google Ads API error: {'; '.join(error_messages)}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        raise Exception(f"Error researching keyword: {str(e)}")

def main():
    """Command line interface for keyword research"""
    # Get keyword from command line argument or use default
    keyword = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_KEYWORD
    
    try:
        data = get_keyword_data(keyword)
        
        if data.get('exact_match', True):
            print(f"Keyword: {data['keyword']}")
            print(f"Avg monthly searches: {data['avg_monthly_searches']}")
            print(f"Competition: {data['competition']}")
            
            if data.get('monthly_breakdown'):
                print("\nMonthly breakdown:")
                for month, searches in data['monthly_breakdown'].items():
                    print(f"{month}: {searches}")
        else:
            print(f"Exact keyword '{keyword}' not returned. Here are some close ideas:")
            for suggestion in data.get('suggestions', []):
                print(f"{suggestion['keyword']}: {suggestion['avg_monthly_searches']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
