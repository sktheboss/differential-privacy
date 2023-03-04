from .messages import RESPONSE_STATUS


class Response:
    def __init__(self, status=RESPONSE_STATUS.get('success'), data=None, message=None):
        self.status = status
        self.data = data
        self.message = message
