from collections import defaultdict
from datetime  import datetime, timedelta
from wsgiref.types import StartResponse, WSGIEnvironment
from flask import Flask, Request, Response, request, make_response
from abc import ABC, abstractmethod

# https://github.com/shubhamharitash/ApiRateLimiter_Core_Java/blob/master/src/main/java/TokenBucketApplication.java

# token bucket and other techniques https://www.enjoyalgorithms.com/blog/design-api-rate-limiter

# creating middlewares https://medium.com/swlh/creating-middlewares-with-python-flask-166bd03f2fd4

class TokenBucket():
    def __init__(self, bucket_size: int, timespan_for_refill_in_milliseconds: int = 1000):
        self.timespan_for_refill : timedelta = timedelta(milliseconds=timespan_for_refill_in_milliseconds)
        self.bucket_size = bucket_size

        self.tokens = bucket_size
        self.last_refill_datetime = datetime.now()

    def _refill_bucket_when_required(self):
        if datetime.now() - self.last_refill_datetime > self.timespan_for_refill:
            self.tokens = self.bucket_size
            self.last_refill_datetime = datetime.now()

    def  get_token(self):
        # refill bucket if the interval for re-filling has passed since last request
        self._refill_bucket_when_required()
        # give a token
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def  refill(self):
        self.tokens = self.bucket_size

class APIRateLimiterBase(ABC):
    @abstractmethod
    def can_request_go_through(self, request):
        pass
    
    @abstractmethod
    def get_retry_after_message():
        pass

class APIRateLimiterTokenBucket(APIRateLimiterBase):
    def __init__(self, bucket_size: int, timespan_for_refill_in_milliseconds: int):
        # TODO: load from configuration

        # if a key of the defaultdict is accessed that doesn't exist, it will create a new TokenBucket for that key
        self.token_buckets = defaultdict(lambda: TokenBucket(bucket_size=bucket_size, timespan_for_refill_in_milliseconds=timespan_for_refill_in_milliseconds))


    def _get_rate_limited_key(self, request: Request):
        api_key = request.headers.get('X-API-Key')
        client_id = api_key if api_key else self._get_client_ip(request)
        return client_id

    def _get_client_ip(self, request: Request):
        """
        Extracts the client's IP address from the request.
        Handles cases where the request is behind a proxy or load balancer.
        """
        # Check the X-Forwarded-For header first
        if 'X-Forwarded-For' in request.headers:
            return request.headers['X-Forwarded-For'].split(',')[0].strip()
        else:
            return request.remote_addr

    
    def can_request_go_through(self, request: Request):
        self.token_buckets[self._get_rate_limited_key(request)].get_token()

    def get_retry_after_timespan_in_second(self, request: Request):
        key = self._get_rate_limited_key(request)
        return int(self.token_buckets[key].timespan_for_refill.total_seconds())






# https://medium.com/swlh/creating-middlewares-with-python-flask-166bd03f2fd4

class APIRateLimiterMiddleware():
    # Inspect HTTP requests to determine the key for the token bucket
    # if new key create in dictionary a new TokenBucket
    # get_token
    # if true forward request to the API

    def __init__(self, wsgi_app, bucket_size, timespan_for_refill_in_milliseconds):

        self.wsgi_app = wsgi_app  # setting up the api rate limiter as middleware
        self.rate_limiter = APIRateLimiterTokenBucket(bucket_size=bucket_size, timespan_for_refill_in_milliseconds=timespan_for_refill_in_milliseconds)
        

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse):
        request = Request(environ)
    
        # Check if the client has available tokens
        if self.rate_limiter.can_request_go_through(request):
            # Forward the request to the actual API endpoint
            return self.wsgi_app(environ, start_response)
        else:
            # Update the Retry-After header and return a 429 Too Many Requests response
            retry_after = int(self.token_buckets[client_id].timespan_for_refill.total_seconds())
            # response = make_response("Too Many Requests", 429)
            response = Response("Too Many Requests", mimetype= 'text/plain', status=429)
            response.headers['Retry-After'] = str(retry_after)
            return response(environ, start_response)



app = Flask('Test_APIRateLimiter')

# Apply the rate limiter as a middleware
app.wsgi_app = APIRateLimiterMiddleware(app.wsgi_app, bucket_size=5, timespan_for_refill_in_milliseconds=10000)

@app.route('/good_fortune', methods=['GET'])
def get_good_fortune():
    api_key = request.headers.get('X-API-Key')
    return f"Your good fortune for today, API key {api_key}: You will have a great day!"

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)