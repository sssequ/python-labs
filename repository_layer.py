from abc import ABC, abstractmethod


# слой репозитория: общий набор операций для любого хранилища
class Repository(ABC):
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get(self, item_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def delete(self, item_id):
        pass


# хранит сущности в словаре до закрытия программы
class MemoryRepository(Repository):
    def __init__(self):
        self._items = {}
        self._next_id = 1

    # сохраняет новый объект и назначает ему id
    def add(self, item):
        if item.id is not None:
            raise ValueError("объект уже был сохранён")

        item.id = self._next_id
        self._items[item.id] = item
        self._next_id += 1
        return item

    # находит объект по id
    def get(self, item_id):
        if item_id not in self._items:
            raise ValueError(f"объект с id {item_id} не найден")

        return self._items[item_id]

    # возвращает список всех объектов
    def get_all(self):
        return list(self._items.values())

    # заменяет сохранённый объект
    def update(self, item):
        self.get(item.id)
        self._items[item.id] = item
        return item

    # удаляет объект по id
    def delete(self, item_id):
        self.get(item_id)
        del self._items[item_id]
