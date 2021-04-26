from mycroft import MycroftSkill, intent_file_handler


class CarStarter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('starter.car.intent')
    def handle_starter_car(self, message):
        self.speak_dialog('starter.car')


def create_skill():
    return CarStarter()

