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

  if utils.checkIsTriangle(AB, AC, BC):
    print("Day la tam giac")
  else:
    print("Day khong phai tam giac")

if __name__ == '__main__':
  main()




