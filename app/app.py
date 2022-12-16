import json
import logging
import random
import time


class TestCase:
    
    def __init__(self):
        logging.basicConfig(
        level="INFO",
        format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
        )
        self.logger = logging.getLogger(__name__)
    
    def bid_ask(self):
        while True:
            msg = dict()
            for level in range(50):
                (
                    msg[f"bid_{str(level).zfill(2)}"],
                    msg[f"ask_{str(level).zfill(2)}"],
                ) = (
                    random.randrange(1, 100),
                    random.randrange(100, 200),
                )
            msg["stats"] = {
                "sum_bid": sum(v for k, v in msg.items() if "bid" in k),
                "sum_ask": sum(v for k, v in msg.items() if "ask" in k),
            }
            self.logger.info(f"{json.dumps(msg)}")
            if msg['ask_01'] + msg['bid_01'] < 105:
                self.slack_notification()
            time.sleep(0.001)

    def slack_notification(self):
        '''
        Что бы включить уведосления, нужен токен слака
        в Dockerfile раскомментировать RUN pip install slack-notifications
        
        import os
        import slack_notifications as slack
        
        slack.ACCESS_TOKEN = 'xxx'
        slack.send_notify('channel-name', username='Bot', text='Alert: ask01+bid01<105')
        '''
        print("ALERT!")
 
 
if __name__ == "__main__":
    TestCase().bid_ask()
