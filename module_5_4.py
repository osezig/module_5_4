class House:
    # Дополнено - домашняя работа по уроку "Различие атрибутов класса и экземпляра"
    houses_history = []  # атрибут будет хранить названия созданных объектов
    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if args:
            name = args[0]
            cls.houses_history.append(name)
        return instance

    def __init__(self, name, number_of_floor):
        self.new_floor = None
        self.name = name
        self.number_of_floor = int(number_of_floor)

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, new_floor):
            print(i)
        if new_floor > self.number_of_floor or new_floor < 1:
            print('-Такого этажа не существует-')
        else:
            print(f'Мы поедем на {new_floor} этаж')
            
            # Домашняя работа по уроку "Специальные методы классов"
    def __len__(self):# - должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floor
    def __str__(self):# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>"
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"

            # Домашняя работа по уроку "Перегрузка операторов"
    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor
    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor
    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor
    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor
    def __add__(self, value):
        if isinstance(value, (int, float)):
            return self.number_of_floor + value
        else:
            raise TypeError("Unsupported type for addition")
    def __radd__(self, value):
        if isinstance(value, (int, float)):
            return self.number_of_floor + value
        else:
            raise TypeError("Unsupported type for addition")
    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.number_of_floor += value
            return self
        else:
            raise TypeError("Unsupported type for addition")
    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')

H1 = House('ЖК Кирпичи', 23)
print(f'Название объекта недвижимости - {H1.name}, этажность здания - {H1.number_of_floor}')
H2 = House('ЖК Акация', 20)
H1.go_to(12)
# __str__
print(H1)
# __len__
print(len(H1))

print(H1 == H2) # __eq__

H1 = H1 + 10 # __add__
print(H1)

H1 += 10 # __iadd__
print(H1)

H2 = 10 + H2 # __radd__
print(H2)
print(H1 > H2) # __gt_
print(H1 >= H2) # __ge__
print(H1 < H2) # __lt__
print(H1 <= H2) # __le__
print(H1 != H2) # __ne__

result = H2 + 2
print(result)
result2 = 10 + H2
print(result2)


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2
del h3
input()