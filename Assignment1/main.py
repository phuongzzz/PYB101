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

  AB = utils.calculateDistance(pointA, pointB)
  AC = utils.calculateDistance(pointA, pointC)
  BC = utils.calculateDistance(pointB, pointC)

  print(f"Do dai AB: { AB }")
  print(f"Do dai AC: { AC }")
  print(f"Do dai BC: { BC }")

  # check co phai tam giac hay khong?
  if utils.checkIsTriangle(AB, AC, BC):
    print("Day la tam giac")
  else:
    print("Day khong phai tam giac")
    return

  # tinh goc giua vector
  vBA = utils.calculateVector(pointB, pointA)
  vAC = utils.calculateVector(pointA, pointC)

  vAB = utils.calculateVector(pointA, pointB)
  vBC = utils.calculateVector(pointB, pointC)

  vCB = utils.calculateVector(pointC, pointB)
  vCA = utils.calculateVector(pointC, pointA)

  print(f"goc BAC: { utils.goc(vBA, vAC) }")
  print(f"goc ABC: { utils.goc(vBA, vBC) }")
  print(f"goc ACB: { utils.goc(vCA, vCB) }")

  # check loai tam giac
  print(utils.typeTriangle(pointA, pointB, pointC))

  # tinh dien tich tam giac
  print(f"dien tich tam giac: {utils.areaOfTriangle(pointA, pointB, pointC)}")

  # do dai cac duong trung tuyen
  utils.altitudeOfTriangle(pointA, pointB, pointC)

  # Toa do trong tam
  print(f"trong tam tam giac: { utils.medianPointOfTriangle(pointA, pointB, pointC) }")

if __name__ == '__main__':
  main()




