# Задание 1

# import random
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def play_random_track(self):
#         random_track = random.choice(self.tracklist)
#         print("Случайный трек:", random_track)
#
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# print("Название:", album4.title)
# print("Исполнитель:", album4.artist)
# print("Год:", album4.release_year)
# print("Жанр:", album4.genre)
# print("Треки:", album4.tracklist)
# album4.play_random_track()

# Задание 2

# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())

# Задание 3

# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print("Ингредиенты", self.name + ":")
#         for ingredient in self.ingredients:
#             print(ingredient)
#
#     def cook(self):
#         print("Готовим", self.name + "!")
#         print("Блюдо", self.name, "готово!")
#         print()
#
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
#
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()

# Задание 5

# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []
#
#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append("Внесение наличных на счет: " + str(amount))
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append("Снятие наличных: " + str(amount))
#         else:
#             print("Недостаточно средств")
#
#     def add_interest(self):
#         interest = self.__balance * self.__interest_rate
#         self.__balance += interest
#         self.__transactions.append("Начислены проценты по вкладу: " + str(interest))
#
#     def history(self):
#         for transaction in self.__transactions:
#             print(transaction)
#
# account = BankAccount(100000, 0.05)
# account.deposit(15000)
# account.withdraw(7500)
# account.add_interest()
# account.history()

# Задание 6

# class Employee:
#     def __init__(self, name, age, salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary
#         self.__bonus = 0
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_bonus(self, bonus):
#         self.__bonus = bonus
#
#     def get_bonus(self):
#         return self.__bonus
#
#     def get_total_salary(self):
#         return self.__salary + self.__bonus
#
# employee = Employee("Марина Арефьева", 30, 90000)
# employee.set_bonus(15000)
#
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())

# Задание 7

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(self.name, "подает голос")
#
#     def move(self):
#         print(self.name, "дергает хвостом")
#
#
# class Dog(Animal):
#     def __init__(self, name, species, legs, breed):
#         super().__init__(name, species, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(self.breed, self.name, "лает")
#
#
# class Bird(Animal):
#     def __init__(self, name, species, legs, wingspan):
#         super().__init__(name, species, legs)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(self.species, self.name, "летит")
#
#
# dog = Dog("Геральт", "доберман", 4, "доберман")
# bird = Bird("Вася", "попугай", 2, "средний")
#
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()

# Задание 10

# class Soldier:
#     def __init__(self, name, rank, service_number):
#         self.name = name
#         self.__rank = rank
#         self.__service_number = service_number
#
#     def get_rank(self):
#         return self.__rank
#
#     def confirm_service_number(self):
#         return self.__service_number
#
#     def promote(self):
#         if self.__rank == "рядовой":
#             self.__rank = "ефрейтор"
#             print(f"{self.name} повышен в звании, он теперь {self.__rank}")
#         else:
#             print(f"{self.name} уже имеет более высокое звание")
#
#     def demote(self):
#         if self.__rank == "ефрейтор":
#             self.__rank = "рядовой"
#             print(f"{self.name} понижен в звании, он теперь {self.__rank}")
#         else:
#             print(f"{self.name} уже имеет более низкое звание")
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
# print("Создан новый игровой персонаж типа Soldier с атрибутами:", vars(soldier1))
# print("Персонаж", soldier1.name, "имеет звание", soldier1.get_rank())
# soldier1.promote()
# soldier1.demote()