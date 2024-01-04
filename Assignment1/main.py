import math
import utils
from point import Point

def main():
  print("PYB101x - Assignment 01")
  xA = int(input("Nhap xA: "))
  yA = int(input("Nhap yA: "))
  pointA = Point(xA, yA)

  xB = int(input("Nhap xB: "))
  yB = int(input("Nhap yB: "))
  pointB = Point(xB, yB)

  xC = int(input("Nhap xC: "))
  yC = int(input("Nhap yC: "))
  pointC = Point(xC, yC)

  AB = utils.khoangcach(pointA, pointB)
  AC = utils.khoangcach(pointA, pointC)
  BC = utils.khoangcach(pointB, pointC)

  print(f"Do dai AB: { AB }")
  print(f"Do dai AC: { AC }")
  print(f"Do dai BC: { BC }")

  # kiểm tra có phải tam giác hay không?
  if utils.kiemtra_tamgiac(AB, AC, BC):
    print("Day la tam giac")
  else:
    print("Day khong phai tam giac")
    return

  # Tính góc giữa 2 vector
  vBA = utils.calculateVector(pointB, pointA)
  vAC = utils.calculateVector(pointA, pointC)

  vAB = utils.calculateVector(pointA, pointB)
  vBC = utils.calculateVector(pointB, pointC)

  vCB = utils.calculateVector(pointC, pointB)
  vCA = utils.calculateVector(pointC, pointA)

  print(f"goc BAC: { utils.goc(vBA, vAC) }")
  print(f"goc ABC: { utils.goc(vBA, vBC) }")
  print(f"goc ACB: { utils.goc(vCA, vCB) }")

  # Kiểm tra loại của tam giác (vuông, nhọn,...)
  print(utils.loai_tamgiac(pointA, pointB, pointC))

  # Tính và in ra diện tích tam giác
  print(f"dien tich tam giac: {utils.dientich_tamgiac(pointA, pointB, pointC)}")

  # Tính và in ra các đường cao của tam giác
  print(f"duong cao tam giac: {utils.duongcao_tamgiac(pointA, pointB, pointC)}") 

  # Tính và in ra các đường trung tuyến của tamgiacs
  utils.trungtuyen_tamgiac(pointA, pointB, pointC)

  # In ra toạ độ trọng tâm của tam giác
  print(f"trong tam tam giac: { utils.trongtam_tamgiac(pointA, pointB, pointC) }")

if __name__ == '__main__':
  main()




