import math
from vector import MyVector
from point import Point

def calculateDistance(firstPoint, secondPoint):
  deltaX = firstPoint.x - secondPoint.x
  deltaY = firstPoint.y - secondPoint.y

  return math.sqrt(deltaX ** 2  + deltaY ** 2)

def checkIsTriangle(edge1, edge2, edge3):
   return ((edge1 + edge2) > edge3) and ((edge1 + edge3) > edge2) and ((edge2 + edge3) > edge1)

def calculateVector(firstPoint, secondPoint):
   x = secondPoint.x - firstPoint.x
   y = secondPoint.y - firstPoint.y
   return MyVector(x,y)

def goc(firstVector, secondVector):
   a = (firstVector.x * secondVector.x) + (firstVector.y * secondVector.y)
   b = math.sqrt(firstVector.x ** 2 + firstVector.y ** 2) * math.sqrt(secondVector.x ** 2 + secondVector.y ** 2)
   cos = a / b
   result = math.degrees(math.acos(cos))
   return round(result, 2)

def typeTriangle(pointA, pointB, pointC):
  vBA = calculateVector(pointB, pointA)
  vAC = calculateVector(pointA, pointC)

  vAB = calculateVector(pointA, pointB)
  vBC = calculateVector(pointB, pointC)

  vCB = calculateVector(pointC, pointB)
  vCA = calculateVector(pointC, pointA)

  gocBAC = goc(vBA, vAC)
  gocABC = goc(vBA, vBC)
  gocACB = goc(vCA, vCB)

  AB = calculateDistance(pointA, pointB)
  AC = calculateDistance(pointA, pointC)
  BC = calculateDistance(pointB, pointC)

  if gocBAC == 90:
    if AB == AC:
      return "Tam giac ABC vuong can tai A"
    else:
      return "Tam giac ABC vuong tai A"
  elif gocACB == 90:
    if AC == BC:
      return "Tam giac ABC vuong can tai C"
    else:  
     return "Tam giac ABC vuong tai C"
  elif gocABC == 90:
    if AB == BC:
      return "Tam giac ABC vuong can tai B"
    else:
     return "Tam giac ABC vuong tai B"
  elif gocBAC > 90:
    if AB == AC:
      return "Tam giac ABC tu can tai A"
    else:
      return "Tam giac ABC tu tai A"
  elif gocACB > 90:
    if AC == BC:
      return "Tam giac ABC tu can tai C"
    else:  
     return "Tam giac ABC tu tai C"
  elif gocABC > 90:
    if AB == BC:
      return "Tam giac ABC tu can tai B"
    else:
      return "Tam giac ABC tu tai B"
  elif AB == AC == BC:
    return "Tam giac ABC deu"
  else:
    return "Tam giac ABC la tam giac thuong"


def areaOfTriangle(pointA, pointB, pointC):
  a = calculateDistance(pointA, pointB)
  b = calculateDistance(pointA, pointC)
  c = calculateDistance(pointB, pointC)

  p = (a + b + c) / 2
  result = math.sqrt(p * (p - a) * (p - b) * (p - c))

  return round(result, 2)

def altitudeOfTriangle(pointA, pointB, pointC):
  a = calculateDistance(pointA, pointB)
  b = calculateDistance(pointA, pointC)
  c = calculateDistance(pointB, pointC)

  p = (a + b + c) / 2

  altitudeFromA = (2 * math.sqrt(p)) / c
  altitudeFromB = (2 * math.sqrt(p)) / b
  altitudeFromC = (2 * math.sqrt(p)) / a

  print(f"Duong cao ha tu A: {altitudeFromA}")
  print(f"Duong cao ha tu B: {altitudeFromB}")
  print(f"Duong cao ha tu C: {altitudeFromC}")

def calculateMedianLine(pointA, pointB, pointC):
  AB = calculateDistance(pointA, pointB)
  AC = calculateDistance(pointA, pointC)
  BC = calculateDistance(pointB, pointC)

  mA = math.sqrt((0.5 * (AB ** 2 + AC ** 2)) - (0.25 * BC ** 2))
  mB = math.sqrt((0.5 * (AB ** 2 + BC ** 2)) - (0.25 * AC ** 2)) 
  mC = math.sqrt((0.5 * (AC ** 2 + BC ** 2)) - (0.25 * AB ** 2))

  print(f"trung tuyen ke tu A: { mA }")
  print(f"trung tuyen ke tu B: { mB }")
  print(f"trung tuyen ke tu C: { mC }")

def medianPointOfTriangle(pointA, pointB, pointC):
  x = (pointA.x + pointB.x + pointC.x)/3
  y = (pointA.y + pointB.y + pointC.y)/3
  return Point(x, y)