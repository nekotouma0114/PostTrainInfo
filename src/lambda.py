import json
import os

import main

def lambda_handler(event, context):
    main.main(os.environ['SLACK_TOKEN'],os.environ['SLACK_CHANNEL'],os.environ['LINES'].split(","))
