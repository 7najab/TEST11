from typing import Dict, List

class Costume:
    """Клас, що представляє костюм (легковаговий об'єкт)."""
    def __init__(self, costume_type: str):
        self.costume_type = costume_type
    
    def display(self, actor_name: str, scene: str):
        print(f"Актор {actor_name} одягнений у {self.costume_type} для сцени '{scene}'.")

class CostumeFactory:
    """Фабрика костюмів для управління екземплярами."""
    _costumes: Dict[str, Costume] = {}

    @staticmethod
    def get_costume(costume_type: str) -> Costume:
        if costume_type not in CostumeFactory._costumes:
            CostumeFactory._costumes[costume_type] = Costume(costume_type)
        return CostumeFactory._costumes[costume_type]

class Actor:
    """Клас, що представляє актора, який може змінювати костюми."""
    def __init__(self, name: str):
        self.name = name
    
    def perform(self, costume_type: str, scene: str):
        costume = CostumeFactory.get_costume(costume_type)
        costume.display(self.name, scene)


actors = [Actor(f"Актор {i+1}") for i in range(5)]  
scenes = [
    ("Сцена 1", "Селянський костюм", [0, 1, 2]),
    ("Сцена 2", "Військовий костюм", [2, 3]),
    ("Сцена 3", "Королівський костюм", [0, 4]),
    ("Сцена 4", "Селянський костюм", [1, 3, 4]),
    ("Сцена 5", "Військовий костюм", [0, 2, 4]),
]

for scene, costume, actor_indices in scenes:
    for index in actor_indices:
        actors[index].perform(costume, scene)