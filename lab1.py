# пользователь мессенджера
class User:
    def __init__(self, name):
        # проверяет тип имени
        if not isinstance(name, str):
            raise TypeError("имя пользователя должно быть строкой")

        # разрешает только латинские буквы без пробелов
        if not name.isascii() or not name.isalpha():
            raise ValueError("имя должно содержать только английские буквы")

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
        if not isinstance(sender, User):
            raise TypeError("отправитель должен быть пользователем")

        self.sender = sender
        self.is_read = False

        # использует общую проверку текста при создании и редактировании
        self.edit(text)

    # изменяет текст сообщения
    def edit(self, new_text):
        if not isinstance(new_text, str):
            raise TypeError("текст сообщения должен быть строкой")

        if not new_text.strip():
            raise ValueError("сообщение не должно быть пустым")

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
        if not isinstance(user, User):
            raise TypeError("участник чата должен быть пользователем")

        if user not in self.users:
            self.users.append(user)

    # отправляет сообщение от участника чата
    def send_message(self, sender, text):
        if sender not in self.users:
            raise PermissionError("отправитель не состоит в чате")

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

    # регистрирует пользователя с уникальным именем
    def register_user(self, name):
        user = User(name)

        for existing_user in self.users:
            if existing_user.name.lower() == user.name.lower():
                raise ValueError("это имя пользователя уже занято")

        self.users.append(user)
        return user

    # создаёт новый чат
    def create_chat(self, name):
        chat = Chat(name)
        self.chats.append(chat)
        return chat