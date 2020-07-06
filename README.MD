# 概要

AWS lambdaでtetudo.com様のRSS情報より電車の遅延情報等を取得してSlackに投稿するもの

# 注意

本プログラムを利用する場合はRSS提供元の利用規約を確認・同意の上ご利用ください
https://aiasahi.jp/term/rss.htm


# 設定

以下を実行(sam、lambdaでの実行用)

```bash
pip install -r requirements.txt -t ./src/lib/
```

`environment.json`をリポジトリ直下に作成
```json:environment.json
{
    "ChangeSlackStatusProject": {
        "SLACK_TOKEN": "Slackのtoken",
        "SLACK_CHANNEL": "投稿するチャンネルのID",
        "LINES": "検索対象の路線名もしくは鉄道会社名を「,」区切りで記載 ex) 山手線,北陸新幹線"
    }
}
```

# 実行

```
sam local invoke -n environment.json
```

# デプロイ

(準備中)