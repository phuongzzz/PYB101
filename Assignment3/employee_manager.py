from employee import Employee
import json

class EmployeeManager:
  list_employees = []
  list_departments = []

  def __init__(self):
    self.readEmployeesFromFiles()

  def addNewEmployee(self):
    print("----")
    print("Thêm nhân viên mới...")
    id = int(input("Nhập mã số: "))
    department_id = int(input("Nhập mã bộ phận: "))
    position = input("Nhập chức vụ (NV / QL): ")
    name = input("Nhập họ và tên: ")
    salary_base = float(input("Nhập hệ sô lương: "))
    working_days = int(input("Nhập số ngày làm việc: "))
    working_performance = float(input("Nhập hệ số hiệu quả: "))
    bonus = float(input("Nhập thưởng: "))
    late_comming_days = int(input("Nhập số ngày đi muộn: "))
    e = Employee(id, name, salary_base, working_days, department_id,
                working_performance, bonus, late_comming_days)
    
    for employee in self.list_employees:
      if employee.id == e.id:
        print("Employee {} is exist!", e.name)
      else:
        print("\nĐã thêm nhân viên mới ...")
        print("----")
        self.list_employees.append(e)
        self.writeEmployeeToFiles()

  def showMenu(self):
    print("""
      1. Hiển thị danh sách nhân viên.
      2. Hiển thị danh sách bộ phận.
      3. Thêm nhân viên mới.
      4. Xóa nhân viên theo ID.
      5. Xóa bộ phân theo ID
      6. Hiển thị bảng lương.
      7: Chinh sua nhan vien.
      7. Thoát.
    """)
    ans = input("Mời bạn nhập chức năng mong muốn: ")
    if ans=="1":
      self.showListEmployees()
    elif ans=="2":
      self.showListDepartments()
    elif ans=="3":
      self.addNewEmployee()
    elif ans=="4":
      self.deleteEmployeeById(1)
    elif ans == "5":
      self.deleteDepartmentById(1)
    elif ans == "7":
      self.editEmployeeById(1)
    elif ans == "8":
      ans = None
    else:
      print("\n Not Valid Choice Try again")

  def writeEmployeeToFiles(self):
    listEmployees = [e.toJSON() for e in self.list_employees]
    jsonData = json.dumps(listEmployees)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonData)
    jsonFile.close()

  def readEmployeesFromFiles(self):
    try:
      f = open("data.json")

      employee_data = json.load(f)
  
      for e in employee_data:
        self.list_employees.append(e)
    except:
      print("file empty...will create a new file after that..")
    
  
  def showListEmployees(self):
    for e in self.list_employees:
      print("----")
      self.showSingleEmployee(e)
      print("----")

  def showListDepartments(self):
    for d in self.list_departments:
      print("----")
      self.showSingleDepartment(d)
      print("----")

  def deleteEmployeeById(self, employeeId):
    results = [e for e in self.list_employees if e.id != employeeId]
    self.list_departments = results

  def deleteDepartmentById(self, departmentId):
    results = [d for d in self.list_departments if d.id != departmentId]
    self.list_departments = results

  def displaySalaryTable(self):
    for e in self.list_employees:
      print("----")
      e.hienThiLuong()
      print("----")
    
  def editEmployeeById(self, employeeId):
    e = next(e for e in self.list_employees if x.id == employeeId )

  def showSingleEmployee(self, employee):
    print("Mã số: {}", employee.id)
    print("Mã bộ phận: {}", employee.department_id)
    # print("Chức vụ: {}", employee.position)
    print("Họ và tên: {}", employee.name)
    print("Hệ số lương: {}", employee.salary_base)
    print("Số ngày làm việc: {}", employee.workingworking_days)
    print("Hệ số hiệu quả: {}", employee.working_performance)
    print("Thưởng: {}", employee.bonus)
    print("Số ngày đi muộn: {}", employee.workinglate_comming_days)

  def showSingleDepartment(self, department):
    print("Mã bộ phận: {}", department.id)
    print("Thưởng bộ phận: {}", department.bonus_salary)