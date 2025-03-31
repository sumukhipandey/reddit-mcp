# src/utils/caching.py
from functools import lru_cache
from datetime import datetime, timedelta

# Simple time-based cache invalidation
cache_timestamps = {}
cache_ttl = timedelta(minutes=5)

def should_invalidate_cache(key):
    """Check if cache for key should be invalidated based on TTL"""
    if key not in cache_timestamps:
        return True
    
    if datetime.now() - cache_timestamps[key] > cache_ttl:
        return True
    
    return False

# Cached Reddit client methods
@lru_cache(maxsize=100)
def get_subreddit_info(subreddit_name):
    """Cached wrapper for getting subreddit info"""
    from src.reddit_client import reddit
    
    # Update cache timestamp
    cache_timestamps[f"subreddit:{subreddit_name}"] = datetime.now()
    
    return reddit.subreddit(subreddit_name)