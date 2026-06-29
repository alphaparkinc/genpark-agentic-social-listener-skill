import os
from typing import List, Dict, Any, Optional

class SocialListenerClient:
    """
    Client SDK for classifying brand mention sentiments and auto-generating customer replies.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("SOCIAL_LISTENER_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def analyze_posts(self, brand_name: str, posts: List[Dict[str, Any]], brand_voice: str) -> List[Dict[str, Any]]:
        """
        Analyzes a batch of posts, identifying positive/negative sentiments and suggesting reply drafts.
        """
        analyzed = []
        
        # Simple sentiment keywords rules for mocking/local execution
        negative_keywords = ["bad", "broken", "issue", "hate", "terrible", "slow", "fail", "annoyed", "wont work"]
        positive_keywords = ["love", "great", "awesome", "perfect", "good", "nice", "excellent", "helpfull"]

        for post in posts:
            text_lower = post["text"].lower()
            sentiment = "neutral"
            urgency = 0.5
            
            # Simple keyword scoring
            neg_matches = sum(1 for kw in negative_keywords if kw in text_lower)
            pos_matches = sum(1 for kw in positive_keywords if kw in text_lower)
            
            if neg_matches > pos_matches:
                sentiment = "negative"
                urgency = min(1.0, 0.5 + (0.1 * neg_matches))
            elif pos_matches > neg_matches:
                sentiment = "positive"
                urgency = max(0.1, 0.5 - (0.1 * pos_matches))
                
            # Draft reply based on sentiment
            if sentiment == "negative":
                reply = f"Hi there! We are very sorry to hear that you are experiencing issues with {brand_name}. Please send us a direct message with your details so we can make this right."
            elif sentiment == "positive":
                reply = f"Thank you so much for the kind words about {brand_name}! We appreciate you sharing your experience."
            else:
                reply = f"Hello! Thanks for mentioning {brand_name}. Let us know if you have any questions or feedback."
                
            analyzed.append({
                "post_id": post["post_id"],
                "sentiment": sentiment,
                "urgency_score": urgency,
                "draft_reply": reply
            })
            
        return analyzed
