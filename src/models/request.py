class AlexaResponse:
    __slots__ = ['title', 'body']

    def __init__(self, title, body):
        self.title = title
        self.body = body

    def get_speech(self):
        speech = dict()
        speech['type'] = 'PlainText'
        speech['text'] = self.body
        return speech

    def build_simple_card(self):
        card = dict()
        card['type'] = 'Simple'
        card['title'] = self.title
        card['content'] = self.body
        return card

    def build_response(self, message, session_attributes={}):
        response = dict()
        response['version'] = '1.0'
        response['sessionAttributes'] = session_attributes
        response['response'] = message
        return response

    def get_statement(self):
        speechlet = dict()
        speechlet['outputSpeech'] = self.get_speech()
        speechlet['card'] = self.build_simple_card()
        speechlet['shouldEndSession'] = True
        return self.build_response(speechlet)