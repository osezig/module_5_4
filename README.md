Задача "История строительства":

Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.

Дополните метод __new__ так, чтобы:

Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:

"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
