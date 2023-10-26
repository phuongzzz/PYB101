class NhanVien:
  def __init__(self, name, month, salary_per_day, day_of_working, coefficient):
    self.name = name
    self.thang = month
    self.luong_co_ban = salary_per_day
    self.he_so_luong = coefficient
    self.ngay_lam_viec = day_of_working
  
  def tinh_luong(self):
    luong_tong =  self.luong_co_ban * self.ngay_lam_viec * self.he_so_luong - 1000000
    if luong_tong > 9000000:
      return int(0.9 * luong_tong)
    return int(luong_tong)

  def hien_thi_luong(self):
    return "Luong cua nhan vien {} nhan duoc trong thang {} la {}".format(self.name, self.thang, self.tinh_luong())

class QuanLy(NhanVien):
  def __init__(self, name, month, salary_per_day, day_of_working, coefficient, performance):
    super().__init__(name, month, salary_per_day, day_of_working, coefficient)
    self.he_so_thuong = performance
  
  def tinh_luong_thuong(self):
    luong_khong_thuong = self.tinh_luong()
    if self.he_so_thuong < 1:
      return int(luong_khong_thuong * self.he_so_thuong)
    else:
      luong_thuong = luong_khong_thuong * (self.he_so_thuong - 1) * 0.85
      return int(luong_khong_thuong + luong_thuong)
    
  def hien_thi_luong(self):
    return "Luong cua nhan vien {} nhan duoc trong thang {} la {}".format(self.name, self.thang, self.tinh_luong_thuong())

def main():
  name = input("Nhap ten = ")
  thang = int(input("Nhap thang = "))
  luong_co_ban = int(input("Nhap LCB = "))
  he_so_luong = float(input("Nhap HSL = "))
  ngay_lam_viec = int(input("Nhap ngay lam viec = "))
  he_so_thuong = float(input("Nhap he so thuong = "))

  nv = QuanLy(name, thang, luong_co_ban, he_so_luong, ngay_lam_viec, he_so_thuong)
  message = nv.hien_thi_luong()
  print(message)

if __name__ == "__main__":
    main()
