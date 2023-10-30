import json

class Employee:
  id = ""
  name = ""
  salary_base = 0
  working_days = 0
  department: 0
  working_performance = 0
  bonus = 0
  late_comming_days = 0

  def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_coming_days):
    self.id = id
    self.name = name
    self.salary_base = salary_base
    self.working_days = working_days
    self.department = department
    self.working_performance = working_performance
    self.bonus = bonus
    self.late_comming_days = late_coming_days
  
  # can tra ra so % luong can dong thue
  def getTaxData():
    pass

  # can tra ra so tien phat di muon
  def getThuongPhatData():
    pass

  def tinhLuong():
    # tổng thu nhập chưa thưởng = (salary_base * working_days) * working_performance
    # Thưởng bộ phận, được lấy từ các Class Department. Chú ý: các quản lý sẽ được thưởng thêm 10% thưởng bộ phận
    # Thưởng riêng cho từng nhân viên, được lấy từ thuộc tính bonus của Class Employee.
    # tổng thu nhập = tổng thu nhập chưa thưởng + bonus + thưởng bộ phận - phạt đi muộn
    # tổng thu nhập chưa thuế = tổng thu nhập * 89.5 %
    # lương thực nhận = tổng thu nhập chưa thuế - khoản thuế cần nộp
    pass

  def hienThiLuong():
    pass

  
  def toJSON(self):
    return self.__dict__