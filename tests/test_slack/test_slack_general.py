import unittest
from src.slack.slack_general import SlackGeneral

class TestSlackGeneral(unittest.TestCase):
    def test_init(self):
        #### success
        #type="user" 
        client = SlackGeneral("user","tests/test_slack/token_files/UserToken.json")
        self.assertEqual(client.get_token(),"Token")

        #type="bot" success case
        clinet = SlackGeneral("bot","tests/test_slack/token_files/BotToken.json")
        self.assertEqual(client.get_token(),"Token")

        #type="user" success case
        client = SlackGeneral("bot","tests/test_slack/token_files/BotToken.json")
        self.assertEqual(client.get_token(),"BotToken")

        ### failure
        #not exists key in file
        with self.assertRaises(KeyError):
            SlackGeneral("bot","tests/test_slack/token_files/FailureToken.json")
        with self.assertRaises(KeyError):
            SlackGeneral("user","tests/test_slack/token_files/FailureToken.json")
        
        with self.assertRaises(FileNotFoundError):
            SlackGeneral("bot","tests/test_slack/token_files/NotExist.json")