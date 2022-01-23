# task3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        # return self._income_wage + self._income_bonus
        return int(self._income['wage']) + int(self._income['bonus'])


pos1 = Position('Ivan', 'Ivanov', 'senior', 15000, 50000)
pos2 = Position('Petr', 'Petrov', 'junior', 5000, 20000)
print(pos1.get_full_name())
print(pos2.get_full_name())
print(pos1.get_total_income())
print(pos2.get_total_income())
