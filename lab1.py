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

# сообщение в мессенджере
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
        self.is_read = False

    # изменяет текст сообщения
    def edit(self, new_text):
        self.text = new_text

    # отмечает сообщение как прочитанное
    def mark_as_read(self):
        self.is_read = True