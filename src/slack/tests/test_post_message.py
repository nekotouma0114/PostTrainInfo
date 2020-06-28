import unittest
from src.post_message import PostMessage
from src.slack_general import SlackReqestError

class TestPostMessage(unittest.TestCase):
    def test_post_message(self):
        """
            Overwrite and use test api
            https://api.slack.com/methods/api.test
            TODO: 成功ケースをどうするかの検討
        """
        client = PostMessage("user","tests/token_files/UserToken.json")
        client.API_URL="https://slack.com/api/api.test"
        with self.assertRaises(SlackReqestError):
            client.post("channel_id","text",option=dict({'key':'value'}))