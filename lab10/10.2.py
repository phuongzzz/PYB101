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

def main():
  name = input("Nhap ten = ")
  thang = int(input("Nhap thang = "))
  luong_co_ban = int(input("Nhap LCB = "))
  he_so_luong = float(input("Nhap HSL = "))
  ngay_lam_viec = int(input("Nhap ngay lam viec = "))

  nv = NhanVien(name, thang, luong_co_ban, he_so_luong, ngay_lam_viec)
  message = nv.hien_thi_luong()
  print(message)

if __name__ == "__main__":
    main()


# Nguyen Hai Phong
# 3, 500000, 20, 1.5
