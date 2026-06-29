import sys
import json
from social_listener import SocialListenerClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Agentic Social Listener Agent Example ===")
    client = SocialListenerClient()
    
    brand_name = "Zenith"
    posts = [
        {"post_id": "p001", "platform": "twitter", "text": "I love the new design of Zenith! It works so smooth and is absolutely perfect!"},
        {"post_id": "p002", "platform": "reddit", "text": "Zenith has been slow lately. The API is broken and keeping throwing errors. Terrible issue."},
        {"post_id": "p003", "platform": "linkedin", "text": "We are evaluating Zenith for our team next quarter."}
    ]
    brand_voice = "Friendly and empathetic"
    
    results = client.analyze_posts(brand_name, posts, brand_voice)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
