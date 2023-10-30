import json
import constants
import urllib.request
import xml.etree.ElementTree as ET
from tax import Tax
from late import Late
import employee_manager

class Employee:

  list_taxes = []
  list_lates = []

  def __init__(self, id, name, salary_base, working_days, department, position, working_performance, bonus, late_coming_days):
    self.id = id
    self.name = name
    self.salary_base = salary_base
    self.working_days = working_days
    self.department = department
    self.working_performance = working_performance
    self.bonus = bonus
    self.late_comming_days = late_coming_days
    self.position = position
  
  # can tra ra so % luong can dong thue
  @classmethod
  def getTaxData(cls):
    print("getting taxes data from:", constants.taxInformationUrl)
    f = urllib.request.urlopen(constants.taxInformationUrl)

    tree = ET.parse(f)
    root = tree.getroot()

    for tax in root.findall('tax'):
      min = int(tax.find('min').text)
      try:
        max = int(tax.find('max').text)
      except:
        max = -1
      
      amount = int(tax.find('value').text)
      tax = Tax(min, max, amount)
      Employee.list_taxes.append(tax)

    print("Tax data:")
    for t in Employee.list_taxes:
      print("min:", t.min)

  # can tra ra so tien phat di muon
  @classmethod
  def getThuongPhatData(cls):
    print("getting data from:", constants.lateInformationUrl)
    f = urllib.request.urlopen(constants.lateInformationUrl)

    list_lates = json.loads(f.read())

    for late in list_lates:
      min = int(late['min'])

      try:
        max = int(late['max'])
      except:
        max = -1
      
      amount = int(late['value'])
      lateObject = Late(min, max, amount)
      Employee.list_lates.append(lateObject)

  def tinhLuong(self):
    # tổng thu nhập chưa thưởng = (salary_base * working_days) * working_performance
    tong_thu_nhap_chua_thuong = (self.salary_base * self.working_days) * self.working_performance

    # Thưởng bộ phận, được lấy từ các Class Department. Chú ý: các quản lý sẽ được thưởng thêm 10% thưởng bộ phận
    department = next(d for d in employee_manager.EmployeeManager.list_departments if d.id == self.department )

    thuong_bo_phan = department.bonus_salary

    if self.position.replace(" ", "").lower() == "ql":
        thuong_bo_phan += (thuong_bo_phan * 0.1)

    # Thưởng riêng cho từng nhân viên, được lấy từ thuộc tính bonus của Class Employee.
    thuong_rieng = self.bonus

    phat_di_muon = self.tinhTienDiMuon()

    # tổng thu nhập = tổng thu nhập chưa thưởng + bonus + thưởng bộ phận - phạt đi muộn
    tong_thu_nhap = tong_thu_nhap_chua_thuong + self.bonus + thuong_bo_phan - phat_di_muon

    # tổng thu nhập chưa thuế = tổng thu nhập * 89.5 %
    tong_thu_nhap_chua_thue = tong_thu_nhap * (0.895)

    tien_thue = self.tinhThue()

    # lương thực nhận = tổng thu nhập chưa thuế - khoản thuế cần nộp
    luong_thuc_nhan = tong_thu_nhap_chua_thue - tien_thue
    return format(luong_thuc_nhan, ",")

  def hienThiLuong(self):
    luong = self.tinhLuong()
    print("----")
    print(f"Ma so: { self.id }")
    print(f"Thu nhập thực nhận: { luong } (VND)")

  def getPosition(self):
    return "Nhân viên" if self.position.replace(" ", "").lower() == "nv" else "Quản lý"
  
  def tinhTienDiMuon(self):
    lateAmount = 0

    # loop để xem số ngày đi muộn rơi vào case nào
    # nếu rơi vào case tối đa (là phần tử cuối) thì k cần check
    for late in Employee.list_lates:
      lastLate = Employee.list_lates[-1]
      if self.late_comming_days > lastLate.min:
        lateAmount = lastLate.amount
        break
      else:
        if late.min <= self.late_comming_days <= late.max:
          lateAmount = late.amount
          break
    
    return lateAmount * self.late_comming_days
  

  def tinhThue(self):
    for tax in Employee.list_taxes:
      lastTax = Employee.list_taxes[-1]
      if self.salary_base > lastTax.min:
        return self.salary_base * lastTax.amount
      else:
        if tax.min <= self.salary_base <= tax.max:
          return self.salary_base * tax.amount
  
  def toJSON(self):
    return self.__dict__