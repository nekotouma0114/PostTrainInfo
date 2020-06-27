import unittest
from src.slack_general import SlackGeneral

class TestSlackGeneral(unittest.TestCase):
    def test_init(self):
        #### success
        #type="user" 
        client = SlackGeneral("user","tests/token_files/UserToken.json")
        self.assertEqual(client.get_token(),"Token")

        #type="bot" success case
        clinet = SlackGeneral("bot","tests/token_files/BotToken.json")
        self.assertEqual(client.get_token(),"Token")

        #type="user" success case
        client = SlackGeneral("bot","tests/token_files/BotToken.json")
        self.assertEqual(client.get_token(),"BotToken")

        ### failure
        #not exists key in file
        with self.assertRaises(KeyError):
            SlackGeneral("bot","tests/token_files/FailureToken.json")
        with self.assertRaises(KeyError):
            SlackGeneral("user","tests/token_files/FailureToken.json")
        
        with self.assertRaises(FileNotFoundError):
            SlackGeneral("bot","tests/token_files/NotExist.json")