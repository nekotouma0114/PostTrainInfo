import feedparser
from datetime import datetime,timezone,timedelta

from slack.post_message import PostMessage
from slack.slack_general import SlackGeneral

def main(token: str,channel_id: str,list_lines: list):
    if not isinstance(list_lines,list):
        raise TypeError("'list_lines' isnt <class 'list'>.")
    
    slack_client = PostMessage(token)
    for info in get_train_info(list_lines):
        slack_client.post(channel_id,generate_message(info))

def get_train_info(list_lines: list) -> list:

    """
        tetsudo.comのRSS情報から指定した路線の情報を取得する
        NOTE: titleは 【{{鉄道名?}}】"."join({{路線名}} みたいな感じで出るっぽいが(2020/07/05時点)パターンは要確認
              ex) 【JR九州】鹿児島本線・肥薩線・指宿枕崎線・日豊本線・日南線・吉都線・特急列車
              上記にinで検索をかけるので鉄道会社でも可能かつ曖昧検索になる
    """
    RSS_URL="http://api.tetsudo.com/traffic/rss20.xml"
    JST = timezone(timedelta(hours=+9))
    now = datetime.now(JST)

    rss_data = feedparser.parse(RSS_URL)
    #NOTE: 前回からの実行時間の差分ではなく固定値で直近１時間を取ってるのでnowのタイミングで取れないデータが出る場合がある
    #      わざわざデータをおく場所を作りたくないのでその点は許容している
    recent_entry = filter(lambda entry: 
                            #TODO: 固定値で1 hourを引き渡してるので後でもうちょっと受け入れ幅を広げる
                            now - datetime_from_rfc822(entry['published']) < timedelta(hours=1) and
                            any(line in entry['title'] for line in list_lines)
                            ,rss_data['entries'])
    for entry in recent_entry:
        yield entry

def generate_message(info: dict) -> str:
    """
        tetsudo.comから取得したRSS情報からslackに投稿するためのメッセージを生成する
    """
    return "{}\n{}".format(info['summary'],info['link'])

def datetime_from_rfc822(dt: str):
    #TODO: tzがついてないやつは多分ValueErrorを吐いて死ぬのでいい感じにする
    return datetime.strptime(dt, '%a, %d %b %Y %H:%M:%S %z')

if __name__ == '__main__':
    main("Token","xxxxxxxxxxx",["肥薩おれんじ鉄道線"])