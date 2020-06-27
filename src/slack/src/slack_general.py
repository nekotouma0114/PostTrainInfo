import json

class SlackGeneral(object):
    """
        Slack API共通の機能を持つ基底クラス
    """

    def __init__(self,token_type: str,token_file: str) -> None:
        """
            SlackのTokenを読み込む
            Parameter:
                type:   token_fileから読み込むtokenの種類。
                        "user" => Tokenを読み込み
                        "bot"  => BotTokenを読み込み
                token_file: SlackのToken情報が記載されたjsonファイルのパス
        """
        allow_token_types = ["bot","user"]

        with open(token_file,"r") as fp:
            config = json.load(fp)
        
        if token_type not in allow_token_types:
            raise ValueError("'token_type' isnt allow value. allow value => {}".format(__allow_token_type))

        self._token = config["Token" if token_type == "user" else "BotToken"]
    
    def get_token(self) -> str:
        return self._token