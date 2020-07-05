import json
import requests

from src.slack.slack_general import SlackGeneral,SlackReqestError

class PostMessage(SlackGeneral):
    API_URL="https://slack.com/api/chat.postMessage"

    def __init__(self,token_type: str,token_file: str):
        super().__init__(token_type,token_file)

    def post(self,channel_id: str,text: str,option: dict = None) -> dict:
        """
            chat.postMessageのAPIを実行する
            必須パラメータ以外はdictで受け取る
            refs:
                chat.postMessage
                https://api.slack.com/methods/chat.postMessage
        """
        post_params = {
            "channel"   : channel_id,
            "text"      : text,
        }
        if option:
            option.update(post_params)
        
        headers = {
            "content-type": "application/json",
            "authorization": "Bearer {}".format(self.get_token())
        }
        print(json.dumps(post_params))
        response = requests.post(self.API_URL,json.dumps(post_params),headers=headers).json()

        if response['ok']:
            return response
        else:
            raise SlackReqestError(response['error'])