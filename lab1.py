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

# чат мессенджера
class Chat:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    # добавляет пользователя в чат
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)

    # создаёт сообщение и добавляет его в чат
    def send_message(self, sender, text):
        message = Message(sender, text)
        self.messages.append(message)
        return message

# групповой чат с названием и описанием
class GroupChat(Chat):
    def __init__(self, name, description=""):
        super().__init__(name)
        self.description = description

    # изменяет название группы
    def rename(self, new_name):
        self.name = new_name

    # изменяет описание группы
    def change_description(self, description):
        self.description = description

# мессенджер хранит пользователей и чаты
class Messenger:
    def __init__(self):
        self.users = []
        self.chats = []

    # регистрирует нового пользователя
    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    # создаёт новый чат
    def create_chat(self, name):
        chat = Chat(name)
        self.chats.append(chat)
        return chat