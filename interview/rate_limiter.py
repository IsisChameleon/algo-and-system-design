"""
Imagine we are building an application that is used by many different customers.
 We want to avoid one customer being able to overload the system by sending too many requests, 
 so we enforce a per-customer rate limit. The rate limit is defined as:
“Each customer can make X requests per Y seconds”
"""
import datetime

# rate limiting algorithm = token bucket

# X-API-Key idendentifies the customer in the header of the request

from collections import defaultdict

class TokenBucket:
    def __init__(self, number_of_tokens: int, interval_for_refilling_tokens: datetime.timedelta):
        self.number_of_tokens = number_of_tokens
        self.current_number_of_tokens = number_of_tokens
        self.interval_for_refilling_tokens = interval_for_refilling_tokens
        self.last_accessed_time  = datetime.datetime.now()
        self.last_refilling_time = datetime.datetime.now()

    def get_token(self):
        current_time = datetime.datetime.now()
        self.last_accessed_time = current_time

        # refill bucket when required
        time_difference = current_time - self.last_refilling_time
        if time_difference > self.interval_for_refilling_tokens:
            self.current_number_of_tokens = self.number_of_tokens
            
        # use a token for the request
        if self.current_number_of_tokens > 0:
            self.current_number_of_tokens -= 1
            return True
        
        # request is rate limited no tokens
        return False


class TokenBucketRateLimiter:
    def __init__(self, number_of_tokens: int, interval_for_refilling_tokens_in_seconds: float):
        self.number_of_tokens = number_of_tokens
        self.interval_for_refilling_tokens = interval_for_refilling_tokens_in_seconds 
        self.token_buckets=defaultdict(lambda: TokenBucket(number_of_tokens, datetime.timedelta(seconds=interval_for_refilling_tokens_in_seconds)))

    def _get_client_key(self, request)->str:
        return request['headers']['X-API-Key']
    
    def _forward_request(self, request):
        print("Request forwarded! ")

    def _reject_request_429(self, request):
        print("Too many requests!!!!")

    def is_this_request_rate_limited(self, request) -> bool:
        client_key = self._get_client_key(request)

        # access the hashmap, find the number of tokens 
        client_tb = self.token_buckets[client_key]

        if (client_tb.get_token()):
            # forward the request
            self._forward_request(request)
            return False
        else:
            self._reject_request_429(request)
            return True

        


