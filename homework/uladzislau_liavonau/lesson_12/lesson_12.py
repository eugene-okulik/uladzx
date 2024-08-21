class Flower:
    def __init__(self, name, color, length, freshness, cost, life_time):
        self.name = name
        self.color = color
        self.length = length  # длина стебля в см
        self.freshness = freshness  # свежесть в днях
        self.cost = cost  # стоимость в $
        self.life_time = life_time  # время жизни в днях

    def __str__(self):
        return (f"{self.name} (Цвет: {self.color}, "
                f"Длина стебля: {self.length} см, "
                f"Свежесть: {self.freshness} дней, "
                f"Стоимость: {self.cost} $, "
                f"Время жизни: {self.life_time} дней)")


class Rose(Flower):
    def __init__(self, color, length, freshness):
        super().__init__("Роза", color, length, freshness, 3, 7)


class Chamomile(Flower):
    def __init__(self, color, length, freshness):
        super().__init__("Ромашка", color, length, freshness, 1, 3)


class Carnation(Flower):
    def __init__(self, color, length, freshness):
        super().__init__("Гвоздика", color, length, freshness, 2, 5)


class FlowersBouquet:
    # cоздание букета (списка)
    def __init__(self):
        self.flowers = []

    # добавление цветов в букет
    def add_flower(self, flower_local):
        self.flowers.append(flower_local)

    # расчёт общей стоимости букета
    def total_cost(self):
        return sum(flower_local.cost for flower_local in self.flowers)

    # расчёт среднего времени жизни букета
    def average_life_time(self):
        return sum(flower_local.life_time for flower_local in self.flowers) / len(self.flowers)

    # сортировка по заданному параметру
    def sort_flowers(self, by="freshness"):
        valid_keys = {
            "freshness": "freshness",
            "color": "color",
            "length": "length",
            "cost": "cost"
        }
        sorting_value = valid_keys.get(by, "freshness")
        self.flowers.sort(key=lambda flower_local: getattr(flower_local, sorting_value), reverse=True)

    # поиск цветов в букете по среднему времени жизни
    def find_flowers_by_life_time(self, min_life_time):
        return [flower_local for flower_local in self.flowers if flower_local.life_time >= min_life_time]

    def __str__(self):
        return "\n".join(str(flower_local) for flower_local in self.flowers)


rose = Rose("Красный", 40, 3)
chamomile = Chamomile("Белый", 15, 4)
carnation = Carnation("Красный", 30, 2)


bouquet = FlowersBouquet()
bouquet.add_flower(rose)
bouquet.add_flower(chamomile)
bouquet.add_flower(carnation)

print("Букет состоит из следующих цветов:")
print(bouquet)

print("\nОбщая стоимость букета:", bouquet.total_cost(), "$")

print("Среднее время жизни букета:", bouquet.average_life_time(), "дней")

bouquet.sort_flowers(by='length')
print("\nБукет после сортировки по заданному параметру:")
print(bouquet)

min_life_time_value = 4
flowers_in_bouquet_with_long_life_time = bouquet.find_flowers_by_life_time(min_life_time=min_life_time_value)
print(f"\nЦветы в букете с временем жизни больше или равным {min_life_time_value} дней:")
for flower in flowers_in_bouquet_with_long_life_time:
    print(flower)
