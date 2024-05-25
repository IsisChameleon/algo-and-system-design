from rate_limiter import TokenBucket, TokenBucketRateLimiter
import unittest
from datetime import timedelta
import time


class TestProgram(unittest.TestCase):
    def test_tokenbucket_case_1(self):
        tb = TokenBucket(2, timedelta(seconds=10))
        self.assertTrue(tb.get_token())
        self.assertTrue(tb.get_token())
        self.assertFalse(tb.get_token())

    def test_tokenbucket_case_2(self):
        tb = TokenBucket(2, timedelta(seconds=1))
        self.assertTrue(tb.get_token())
        self.assertTrue(tb.get_token())
        time.sleep(1)
        self.assertTrue(tb.get_token())

    def test_ratelimiter_1(self):
        rate_limiter = TokenBucketRateLimiter(2, 1.0)

        incoming_request_1 = {'headers': {'X-API-Key': 'test_key_1'}}
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_1))

    def test_ratelimiter_2_clients(self):
        rate_limiter = TokenBucketRateLimiter(2, 1.0)

        incoming_request_1_c1 = {'headers': {'X-API-Key': 'test_key_1'}}
        incoming_request_2_c1 = {'headers': {'X-API-Key': 'test_key_1'}}
        incoming_request_1_c2 = {'headers': {'X-API-Key': 'test_key_2'}}
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_1_c1))
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_2_c1))
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_1_c2))

    def test_ratelimiter_2_clients_(self):
        rate_limiter = TokenBucketRateLimiter(2, 1.0)

        incoming_request_1_c1 = {'headers': {'X-API-Key': 'test_key_1'}}
        incoming_request_2_c1 = {'headers': {'X-API-Key': 'test_key_1'}}
        incoming_request_3_c1 = {'headers': {'X-API-Key': 'test_key_1'}}
        incoming_request_1_c2 = {'headers': {'X-API-Key': 'test_key_2'}}
        print("----------------TEST---------------------------------")
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_1_c1))
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_2_c1))
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_1_c2))
        self.assertTrue(rate_limiter.is_this_request_rate_limited(incoming_request_3_c1))
        time.sleep(1)
        self.assertFalse(rate_limiter.is_this_request_rate_limited(incoming_request_3_c1))

        



if __name__ == '__main__':
    unittest.main()