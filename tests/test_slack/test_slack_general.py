import unittest
from src.slack.slack_general import SlackGeneral

class TestSlackGeneral(unittest.TestCase):
    def test_init(self):
        client = SlackGeneral("Token")
        self.assertEqual(client.get_token(),"Token")