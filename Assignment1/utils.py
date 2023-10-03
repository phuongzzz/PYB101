import math

def calculateDistance(firstPoint, secondPoint):
  deltaX = firstPoint.x - secondPoint.x
  deltaY = firstPoint.y - secondPoint.y

  return math.sqrt(deltaX ** 2  + deltaY ** 2)

def checkIsTriangle(edge1, edge2, edge3):
   return ((edge1 + edge2) > edge3) and ((edge1 + edge3) > edge2) and ((edge2 + edge3) > edge1)
