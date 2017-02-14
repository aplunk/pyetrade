#!/usr/bin/env python3
'''pyetrade authorization unit tests
   TODO:
    * Fix mocking'''

import unittest
from unittest.mock import patch
from pyetrade import authorization

class TestETradeAuthorization(unittest.TestCase):
    '''TestEtradeAuthorization Unit Test'''
    # Mock out OAuth1Session
    @patch('pyetrade.authorization.OAuth1Session')
    def test_get_request_token(self, MockOAuthSession):
        '''test_get_request_token(self, MockOAuthSession)'''
        # Set Mock returns
        MockOAuthSession.fetch_request_token.return_value = "{'oauth_token': 'abc123'}"
        MockOAuthSession().parse_authorization_response().__getitem__.return_value = 'abc123'
        # Setup authorization
        oauth = authorization.ETradeOAuth('xyz321', 'secret')
        self.assertEqual(oauth.get_request_token(), 'https://us.etrade.com/e/t/etws/authorize?key=xyz321&token=abc123')
        self.assertTrue(MockOAuthSession().parse_authorization_response().__getitem__.called)
    # Mock out OAuth1Session
    @patch('pyetrade.authorization.OAuth1Session')
    def test_get_access_token(self, MockOAuthSession):
        '''test_get_access_token(self, MockOAuthSession)'''
        # Set Mock returns
        MockOAuthSession().fetch_access_token.return_value = "{'oauth_token': 'abc', 'oauth_token_secret': 'xyz'}"
        oauth = authorization.ETradeOAuth('xyz321', 'secret')
        oauth.get_request_token()
        self.assertEqual(oauth.get_access_token('abcxyz'), "{'oauth_token': 'abc', 'oauth_token_secret': 'xyz'}")
        self.assertTrue(MockOAuthSession().fetch_access_token.called)