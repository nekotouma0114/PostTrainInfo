import json

class SlackGeneral(object):
    """
        Slack API共通の機能を持つ基底クラス
    """

    def __init__(self,token) -> None:
        """
            SlackのTokenを読み込む
        """
        self._token = token
    
    def get_token(self) -> str:
        return self._token

class SlackReqestError(Exception):
    """
        Slack APIによるreqestにより{"ok" : False}が返却された場合に発生させる用の例外
    """
    pass