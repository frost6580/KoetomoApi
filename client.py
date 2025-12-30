from config import config
import requests
import uuid


class Koetomo:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": config.USER_AGENT,
                "Content-Type": "application/x-www-form-urlencoded",
                "Connection": "keep-alive",
                "X-App-Version": config.APP_VERSION,
            }
        )

        self.token = None
        self.userid = None

    def login(self, email, passwd):
        data = {
            "uid": "1",
            "password": passwd,
            "device_uid": str(uuid.uuid4()),
            "email": email,
            "auth_token": "non_auth",
            "version": config.APP_VERSION,
            "feature": "skwmeshroom,firebase,mail_auth,reset_status,chat_pagination,speaker_applicant,p2p_room,skyway",
        }

        response = self.session.post(
            config.HOST_URL + config.LOGIN_PATH, data=data, timeout=20
        )
        if response.status_code == 200:
            self.token = response.json()["data"]["auth_token"]
            self.userid = response.json()["data"]["user_id"]
            self.post_arrival()
            return response.json()
        else:
            return None

    def post_arrival(self):
        data = {
            "auth_token": self.token,
            "no_unread_chat_count": "1",
            "uid": self.userid,
            "version": config.APP_VERSION,
        }
        self.session.post(config.HOST_URL + config.ARRIVAL_PATH, data=data, timeout=20)

    def get_feed(self, count=50):
        params = {"consistency": "1", "count": count}
        response = self.session.get(
            config.HOST2_URL + config.FEED_PATH, params=params, timeout=20
        )
        if response.status_code == 200:
            return response.json()

    def post_feed(self, text):
        data = {
            "auth_token": self.token,
            "description": text,
            "play_time": "0",
            "uid": self.userid,
            "version": config.APP_VERSION,
        }
        response = self.session.post(
            config.HOST2_URL + config.FEED_PATH, data=data, timeout=20
        )
        if response.status_code == 200:
            return response.json()
    
    def delete_feed(self, id):
        params = {
            "auth_token": self.token,
            "feed_post_id": id,
            "uid": self.userid,
            "version": config.APP_VERSION,
        }
        response = self.session.delete(
            config.HOST2_URL + config.FEED_PATH, params=params, timeout=20
        )
        if response.status_code == 200:
            return response.json()

    def post_comment(self, id, text):
        data = {
            "auth_token": self.token,
            "feed_post_id": id,
            "uid": self.userid,
            "text": text,
            "version": config.APP_VERSION,
        }
        self.session.post(config.HOST_URL + config.COMMENT_PATH, data=data, timeout=20)

    def post_like(self, id):
        data = {
            "auth_token": self.token,
            "feed_post_id": id,
            "uid": self.userid,
            "version": config.APP_VERSION,
        }
        self.session.post(config.HOST_URL + config.LIKE_PATH, data=data, timeout=20)

    def can_send(self, id):
        params = {"target_id": id}
        response = self.session.get(
            config.HOST2_URL + config.CANSEND_PATH, params=params, timeout=20
        )
        if response.status_code == 200:
            return response.json()

    def post_follow(self, id):
        data = {
            "auth_token": self.token,
            "target_id": id,
            "version": config.APP_VERSION,
        }
        self.session.post(config.HOST_URL + config.FOLLOW_PATH, data=data, timeout=20)

    def post_call(self, id):
        data = {
            "auth_token": self.token,
            "call_method": "skyway",
            "origin": "0",
            "target_id": id,
            "uid": self.userid,
            "version": config.APP_VERSION,
        }
        self.session.post(config.HOST_URL + config.REQUESTS_PATH, data=data, timeout=20)

    def post_messages(self, id):
        data = {
            "target_id": id,
            "auth_token": self.token,
            "chat_id": "160710715",
            "version": config.APP_VERSION,
            "message_type": "1",
            "text_message": "テスト",
        }
        self.session.post(config.HOST_URL + config.MESSAGES_PATH, data=data, timeout=20)
