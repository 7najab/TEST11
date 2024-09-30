from abc import ABC, abstractmethod

# Абстрактний клас ювелірного виробу
class Jewelry(ABC):
    def __init__(self, name, weight, complexity, labor_cost):
        self.name = name
        self.weight = weight
        self.complexity = complexity
        self.labor_cost = labor_cost

    @abstractmethod
    def get_price(self):
        pass

    def display_info(self):
        print(f"{self.name}: Вага - {self.weight} г, Складність - {self.complexity}, Ціна - {self.get_price()} грн")

# Клас для золотих виробів
class GoldJewelry(Jewelry):
    def __init__(self, name, weight, complexity, labor_cost, gold_price_per_gram):
        super().__init__(name, weight, complexity, labor_cost)
        self.gold_price_per_gram = gold_price_per_gram

    def get_price(self):
        return self.weight * self.gold_price_per_gram + self.complexity * self.labor_cost

# Клас для срібних виробів
class SilverJewelry(Jewelry):
    def __init__(self, name, weight, complexity, labor_cost, silver_price_per_gram):
        super().__init__(name, weight, complexity, labor_cost)
        self.silver_price_per_gram = silver_price_per_gram

    def get_price(self):
        return self.weight * self.silver_price_per_gram + self.complexity * self.labor_cost

# Абстрактна фабрика для ювелірних виробів
class JewelryFactory(ABC):
    @abstractmethod
    def create_earring(self):
        pass

    @abstractmethod
    def create_ring(self):
        pass

    @abstractmethod
    def create_chain(self):
        pass

# Фабрика для золотих виробів
class GoldJewelryFactory(JewelryFactory):
    def __init__(self, gold_price_per_gram, labor_cost):
        self.gold_price_per_gram = gold_price_per_gram
        self.labor_cost = labor_cost

    def create_earring(self):
        return GoldJewelry("Золоті сережки", 5, 3, self.labor_cost, self.gold_price_per_gram)

    def create_ring(self):
        return GoldJewelry("Золота каблучка", 4, 2, self.labor_cost, self.gold_price_per_gram)

    def create_chain(self):
        return GoldJewelry("Золотий ланцюжок", 20, 4, self.labor_cost, self.gold_price_per_gram)

# Фабрика для срібних виробів
class SilverJewelryFactory(JewelryFactory):
    def __init__(self, silver_price_per_gram, labor_cost):
        self.silver_price_per_gram = silver_price_per_gram
        self.labor_cost = labor_cost

    def create_earring(self):
        return SilverJewelry("Срібні сережки", 5, 3, self.labor_cost, self.silver_price_per_gram)

    def create_ring(self):
        return SilverJewelry("Срібна каблучка", 4, 2, self.labor_cost, self.silver_price_per_gram)

    def create_chain(self):
        return SilverJewelry("Срібний ланцюжок", 20, 4, self.labor_cost, self.silver_price_per_gram)

# Клас для відображення каталогу
class Catalog:
    def __init__(self, factory: JewelryFactory):
        self.factory = factory

    def display_catalog(self):
        earring = self.factory.create_earring()
        ring = self.factory.create_ring()
        chain = self.factory.create_chain()

        earring.display_info()
        ring.display_info()
        chain.display_info()

# Основна функція
def main():
    gold_factory = GoldJewelryFactory(gold_price_per_gram=1500, labor_cost=500)
    silver_factory = SilverJewelryFactory(silver_price_per_gram=100, labor_cost=500)

    while True:
        choice = input("Виберіть категорію (1 - Золото, 2 - Срібло, q - вийти): ")

        if choice == '1':
            print("\nКаталог золотих виробів:")
            gold_catalog = Catalog(gold_factory)
            gold_catalog.display_catalog()
        elif choice == '2':
            print("\nКаталог срібних виробів:")
            silver_catalog = Catalog(silver_factory)
            silver_catalog.display_catalog()
        elif choice.lower() == 'q':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
