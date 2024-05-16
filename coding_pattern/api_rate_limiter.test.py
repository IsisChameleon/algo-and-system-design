import unittest
from unittest.mock import patch, MagicMock
from api_rate_limiter import APIRateLimiterMiddleware,TokenBucket
from datetime  import datetime, timedelta
from time import sleep


class TestTokenBucket(unittest.TestCase):

    def test_init(self):
        tb = TokenBucket(5, 10000)
        self.assertEqual(tb.tokens, 5)
        self.assertEqual(tb.timespan_for_refill, timedelta(milliseconds=10000))
        can_proceed = tb.get_token()
        self.assertEqual(tb.tokens, 4)
        self.assertEqual(True, can_proceed)

    def test_exhaustion(self):
        tb = TokenBucket(1, 10000)
        self.assertEqual(tb.tokens, 1)
        can_proceed = tb.get_token()
        self.assertEqual(True, can_proceed)
        can_proceed = tb.get_token()
        self.assertEqual(False, can_proceed)

    def test_refill(self):
        tb = TokenBucket(1, 1000)
        self.assertEqual(tb.tokens, 1)
        can_proceed = tb.get_token()
        self.assertEqual(True, can_proceed)
        can_proceed = tb.get_token()
        self.assertEqual(False, can_proceed)
        self.assertEqual(tb.tokens, 0)
        sleep(1.1)
        can_proceed = tb.get_token()
        self.assertEqual(True, can_proceed)


class TestAPIRateLimiterMiddleware(unittest.TestCase):
    def setUp(self):
        self.mock_app = MagicMock()
        self.middleware = APIRateLimiterMiddleware(self.mock_app, bucket_size=5, timespan_for_refill_in_milliseconds=1000)

    def test_get_client_ip_from_x_forwarded_for(self):
        mock_request = MagicMock()
        mock_request.headers = {'X-Forwarded-For': '192.168.1.100, 10.0.0.1'}
        self.assertEqual(self.middleware._get_client_ip(mock_request), '192.168.1.100')

    def test_get_client_ip_from_remote_addr(self):
        mock_request = MagicMock()
        mock_request.headers = {}
        mock_request.remote_addr = '10.0.0.1'
        self.assertEqual(self.middleware._get_client_ip(mock_request), '10.0.0.1')

    @patch('api_rate_limiter.datetime')
    def test_token_bucket_get_token_with_refill(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 4, 1, 10, 0, 0)
        self.assertTrue(token_bucket.get_token())
        self.assertEqual(token_bucket.tokens, 4)

        mock_datetime.now.return_value = datetime(2023, 4, 1, 10, 0, 1)
        self.assertTrue(token_bucket.get_token())
        self.assertEqual(token_bucket.tokens, 3)

    @patch('api_rate_limiter.datetime')
    def test_token_bucket_get_token_with_no_refill(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 4, 1, 10, 0, 0)

        for _ in range(5):
            self.assertTrue(token_bucket.get_token())
        self.assertFalse(token_bucket.get_token())

    @patch('api_rate_limiter.datetime')
    def test_middleware_allows_request_with_available_tokens(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2023, 4, 1, 10, 0, 0)
        mock_request = MagicMock()
        mock_request.headers = {'X-API-Key': 'abc123'}

        self.middleware(mock_request.environ, mock_request.start_response)
        self.mock_app.assert_called_once_with(mock_request.environ, mock_request.start_response)

    @patch('api_rate_limiter.datetime')
    def test_middleware_rejects_request_with_no_tokens(self, mock_datetime):
        mock_datetime.now.return_value = datetime        mock_request = MagicMock()
        mock_request.headers = {'X-API-Key': 'abc123'}

        for _ in range(5):
            self.middleware(mock_request.environ, mock_request.start_response)

        response = self.middleware(mock_request.environ, mock_request.start_response)
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.headers['Retry-After'], '60')

if __:
    unittest.main()



if __name__ == '__main__':
    unittest.main()