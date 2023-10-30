from employee import Employee
from department import Department
from manager import Manager
import json

class EmployeeManager:
  list_employees = []
  list_departments = []

  def __init__(self):
    self.readDataFromFile()
    Employee.getTaxData()
    Employee.getThuongPhatData()

  def showMenu(self):
    while True:
      print("""
        1. Hiển thị danh sách nhân viên.
        2. Hiển thị danh sách bộ phận.
        3. Thêm nhân viên mới.
        4. Xóa nhân viên theo ID.
        5. Xóa bộ phân theo ID
        6. Hiển thị bảng lương.
        7: Chỉnh sửa nhân viên.
        8: Thoát.
      """)
      ans = input("Mời bạn nhập chức năng mong muốn: ")
      if ans=="1":
        self.showListEmployees()
      elif ans=="2":
        self.showListDepartments()
      elif ans=="3":
        self.addNewEmployee()
      elif ans=="4":
        self.deleteEmployeeById()
      elif ans == "5":
        self.deleteDepartmentById()
      elif ans == "6":
        self.showSalaryTable()
      elif ans == "7":
        self.editEmployeeById()
      elif ans == "8":
        break
      else:
        print("\n Lựa chọn không hợp lệ, hãy chọn lại!")
        continue

  # Employee related functions
  def addNewEmployee(self):
    print("----")
    print("Thêm nhân viên mới...")
    
    while True:
      try:
        id = input("Nhập mã số: ")
        if not id:
          raise ValueError
      except ValueError:
        print("Mã nhân viên không được để trống, hãy nhập lại!")
        continue
      else:
        try:
          e = next(e for e in EmployeeManager.list_employees if e.id == id )
          if e:
            print("Mã nhân viên đã tồn tại, hãy nhập mã nhân viên khác!") 
            continue
        except:
          break
    
    while True:
      try:
        department_id = input("Nhập mã bộ phận: ")
        if not department_id: raise ValueError
      except ValueError:
        print("Mã bộ phận không được để trống, hãy nhập lại!")
        continue
      else:
        try:
          d = next(d for d in EmployeeManager.list_departments if d.id == department_id )
          if d: break # nếu tồn tại bộ phận rồi thì thôi, chuyển sang bước tiếp
        except: # chưa có thì tạo
          self.addNewDeparment(department_id)
        break
    
    while True:
      try:
        position = input("Nhập chức vụ (NV / QL): ").replace(" ", "").lower()
        if not position:
          raise ValueError
        elif not (position == "nv" or position == "ql"):
          raise ValueError
      except ValueError:
        print("Chức vụ không được bỏ trống và phải đúng format, hãy thử lại!")
        continue
      else:
        break
      
    while True:
      try:
        name = input("Nhập họ và tên: ")
        if not name:
          raise ValueError
      except ValueError:
        print("Tên không được để trống, hãy nhập lại!")
        continue
      else:
        break
    
    while True:
      try:
        salary_base = float(input("Nhập hệ sô lương: "))
        if salary_base <= 0:
          raise ValueError
      except ValueError:
        print("Hệ số lương là số và phải lớn hơn 0, hãy nhập lại!")
        continue
      else:
        break
    
    while True:
      try:
        working_days = int(input("Nhập số ngày làm việc: "))
        if working_days <= 0:
          raise ValueError
      except ValueError:
        print("Số ngày làm việc không được để trống, phải là số nguyên và lớn hơn 0, hãy nhập lại!")
        continue
      else:
        break
    
    while True:
      try:
        working_performance = float(input("Nhập hệ số hiệu quả: "))
        if working_performance <= 0:
          raise ValueError
      except ValueError:
        print("Hệ số hiệu quả không được để trống, phải là số và lớn hơn 0, hãy thử lại!")
        continue
      else:
        break
    
    while True:
      try:
        bonus = float(input("Nhập thưởng: "))
        if bonus <= 0:
          raise ValueError
      except ValueError:
        print("Thưởng không được bỏ trống, phải là số và phải lớn hơn 0, hãy nhập lại!")
        continue
      else:
        break
    
    while True:
      try:
        late_comming_days = int(input("Nhập số ngày đi muộn: "))
        if late_comming_days < 0:
          raise ValueError
      except ValueError:
        print("Số ngày đi muộn không được bỏ trống, phải là số nguyên dương, hãy nhập lại!")
      else:
        break
    
    if position == "nv":
      e = Employee(id, name, salary_base, working_days, department_id, position,
                  working_performance, bonus, late_comming_days)
    elif position == "ql":
      e = Manager(id, name, salary_base, working_days, department_id, position,
                  working_performance, bonus, late_comming_days)
    
    print("new NV: ", e)
    EmployeeManager.list_employees.append(e)
    self.saveChangesToFile()
    print("\nĐã thêm nhân viên mới ...")
    print("----")

  
  def showSalaryTable(self):
    for e in EmployeeManager.list_employees:
      e.hienThiLuong()

  def readEmployeesFromFiles(self):
    print("readEmployeesFromFiles")
    try:
      f = open("./data.json")
      json_data = json.load(f)
      f.close()
    except:
      print("file empty...will create a new file after that..")

    for data in json_data["employees"]:
      position = data["position"]
      if position.replace(" ", "").lower() == "ql":
        e = Manager(
          id = data["id"],
          name = data["name"],
          salary_base = data["salary_base"],
          working_days = data["working_days"],
          department = data["department"],
          working_performance = data["working_performance"],
          bonus = data["bonus"],
          late_coming_days = data["late_comming_days"],
          position = position
        )
      else:
        e = Employee(
          id = data["id"],
          name = data["name"],
          salary_base = data["salary_base"],
          working_days = data["working_days"],
          department = data["department"],
          working_performance = data["working_performance"],
          bonus = data["bonus"],
          late_coming_days = data["late_comming_days"],
          position = position
        )
      EmployeeManager.list_employees.append(e)

  # Hiển thị danh sách nhân viên
  def showListEmployees(self):
    print("Total:", len(EmployeeManager.list_employees))
    for e in EmployeeManager.list_employees:
      print("----")
      self.showSingleEmployee(e)
      print("----")

  # Xoá nhân viên theo Id
  def deleteEmployeeById(self):
    while True:
      try:
        employeeId = input("Nhập id nhân viên cần xoá (Nhập -1 để quay lại menu): ")
        if not employeeId: raise ValueError
      except ValueError:
        print("Id nhân viên không được để trống! hãy nhập lại")
        continue
      else:
        if employeeId == "-1":
          break
        else:
          results = [e for e in EmployeeManager.list_employees if e.id != employeeId]
          EmployeeManager.list_employees = results
          self.saveChangesToFile()
          print("da xoa nhan vien ", employeeId)
          break

  def editEmployeeById(self):
    while True:
      try:
        employeeId = input("Nhập mã nhân viên: ")
        if not employeeId:
          raise ValueError
      except ValueError:
          print("Mã nhân viên không được để trống, hãy nhập lại!")
      else:
        try:
          e = next(e for e in EmployeeManager.list_employees if e.id == employeeId )
          print("Chỉnh sửa nhân viên:", e.name) 
        except:
          print("Không tìm thấy nhân viên!")
          continue
        else:
          break

    newName = input("Nhập họ và tên: ")
    if len(newName) > 0:
      e.name = newName

    while True:
      try:
        salary_base = -1
        salary_base_str = input("Nhập hệ số lương:")

        if len(salary_base_str) > 0:
          salary_base = float(salary_base_str)
          if salary_base < 0:
            raise ValueError
      except ValueError:
          print("Hệ số lương phải là số và là số dương, hãy nhập lại!")
          continue
      else:
          break
    
    if salary_base > 0:
      e.salary_base = salary_base

    while True:
      try:
        working_days = -1
        working_days_str = input("Nhập số ngày làm việc:")

        if len(working_days_str) > 0:
          working_days = int(working_days_str)
          if working_days < 0:
            raise ValueError
      except ValueError:
        print("Số ngày làm việc phải là số nguyên dương, hãy nhập lại!")
        continue
      else:
        break

    if working_days >= 0:
      e.working_days = working_days

    while True:
      try:
        working_performance = -1
        working_performance_str = input("Nhập hệ số hiệu quả:")

        if len(working_performance_str) > 0:
          working_performance = int(working_performance_str)
          if working_performance < 0:
            raise ValueError
      except ValueError:
        print("Hệ số hiệu quả phải là số dương, hãy nhập lại!")
        continue
      else:
        break

    if working_performance > 0:
      e.working_performance = working_performance 

    while True:
      try:
        bonus = -1
        bonus_str = input("Nhập thưởng:")

        if len(bonus_str) > 0:
          bonus = float(bonus_str)
          if bonus < 0:
            raise ValueError
      except ValueError:
        print("Thưởng phải là số dương, hãy nhập lại!")
        continue
      else:
        break

    if bonus > 0:
      e.bonus = bonus 

    while True:
      try:
        late_comming_days = -1
        late_comming_days_str = input("Nhập số ngày đi muộn:")

        if len(late_comming_days_str) > 0:
          late_comming_days = float(late_comming_days_str)
          if late_comming_days < 0:
            raise ValueError
      except ValueError:
        print("Số ngày đi muộn phải là số dương, hãy nhập lại!")
        continue
      else:
        break

    if late_comming_days > 0:
      e.late_comming_days = late_comming_days 
    
    print("----")
    self.showSingleEmployee(e)
    self.saveChangesToFile()
    print("Đã cập nhật thành công!")

  def showSingleEmployee(self, employee):
    print("Mã số:",employee.id)
    print("Mã bộ phận:", employee.department)
    print(f"Chức vụ: { employee.getPosition() }")
    print("Họ và tên:", employee.name)
    print(f"Hệ số lương: { format(employee.salary_base, ',') } (VND)")
    print(f"Số ngày làm việc: { employee.working_days } (ngày)")
    print("Hệ số hiệu quả:", employee.working_performance)
    print(f"Thưởng: { format(employee.bonus, ',') } (VND)")
    print("Số ngày đi muộn:", employee.late_comming_days)

  def readDepartmentsFromFile(self):
    print("readDepartmentsFromFile") 
    try:
      f = open("./data.json")
      json_data = json.load(f)
      for data in json_data["departments"]:
        d = Department(id = data["id"], bonus_salary = data["bonus_salary"])
        EmployeeManager.list_departments.append(d)
      f.close()
    except:
      print("Error when reading Departments data from file!")
  
  # Thêm mới department
  def addNewDeparment(self, department_id):
    print(f"Chưa có bộ phận {department_id}, tiến hành tạo mới")
    while True:
      try:
        bonus_salary = float(input("Nhập thưởng bộ phận: "))
        if not bonus_salary:
          raise ValueError
        elif bonus_salary < 0:
          raise ValueError
      except ValueError:
        print("Thưởng bộ phận không được bỏ trống, phải là số và lớn hơn 0, hãy nhập lại!")
        continue
      else: break

    d = Department(department_id, bonus_salary)
    EmployeeManager.list_departments.append(d)

  # Hiển thị danh sách department
  def showListDepartments(self):
    for d in EmployeeManager.list_departments:
      print("----")
      self.showSingleDepartment(d)
      print("----")

  def deleteDepartmentById(self):
    while True:
      try: 
        departmentId = input("Nhập id phòng ban cần xoá (Nhập -1 để quay lại menu): ").replace(" ", "").lower()
        if not departmentId: raise ValueError
      except ValueError:
        print("Id phòng ban không được để trống, hãy nhập lại")
        continue
      else:
        if departmentId == "-1":
          break
        else:
          results = [d for d in EmployeeManager.list_departments if d.id.replace(" ", "").lower() != departmentId]
          EmployeeManager.list_departments = results
          print("da xoa phong ban ", departmentId)
          break
    
    for d in EmployeeManager.list_departments:
      print(d.id)

  def displaySalaryTable(self):
    for e in EmployeeManager.list_employees:
      print("----")
      e.hienThiLuong()
      print("----")

  def showSingleDepartment(self, department):
    print("Mã bộ phận:", department.id)
    print(f"Thưởng bộ phận: { format(department.bonus_salary, ',') } (VND)")
  
  def saveChangesToFile(self):
    listEmployees = [e.toJSON() for e in EmployeeManager.list_employees]
    listDepartments = [d.toJSON() for d in EmployeeManager.list_departments]
    myDict = {"employees": listEmployees, "departments": listDepartments}

    jsonData = json.dumps(myDict)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonData)
    jsonFile.close()
  
  def readDataFromFile(self):
    self.readEmployeesFromFiles()
    self.readDepartmentsFromFile()