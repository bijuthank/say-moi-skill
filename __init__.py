from mycroft import MycroftSkill, intent_file_handler


class SayMoi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('moi.say.intent')
    def handle_moi_say(self, message):
        self.speak_dialog('moi.say')


def create_skill():
    return SayMoi()

