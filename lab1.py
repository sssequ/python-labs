# пользователь мессенджера
class User:
    def __init__(self, name):
        self.name = name
        self.is_online = False

    # переводит пользователя в статус онлайн
    def login(self):
        self.is_online = True

    # переводит пользователя в статус офлайн
    def logout(self):
        self.is_online = False
