class Department:

  def __init__(self, id, bonus_salary):
    self.id = id
    self.bonus_salary = bonus_salary

  def toJSON(self):
    return self.__dict__