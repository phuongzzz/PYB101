import json

def calculateAvgPoint(listPointsString):
  listPoints = [float(s) for s in listPointsString.split(",")]
  avgPoint = 0
  if len(listPoints) == 4:
     avgPoint = listPoints[0] * 0.05 + listPoints[1] * 0.1 + listPoints[2] * 0.15 + listPoints[3] * 0.7
  elif len(listPoints) == 5:
    avgPoint = listPoints[0] * 0.05 + listPoints[1] * 0.1 + listPoints[2] * 0.1 + listPoints[3] * 0.15 + listPoints[4] * 0.6
  else: return 0
  return round(avgPoint, 2)
   

def tinhdiem_trungbinh(filePath):
  
  f = open(filePath, "r")

  # read the firstline and put the result to set
  columnNames = f.readline().replace("\n", "").replace(" ", "").split(",")

  listStudents = []
  lines = f.readlines()

  # read each information of student
  for line in lines:
    currentStudentPoints = line.replace("\n", "").replace(" ", "").split(";")

    studentDict = {}
    pointDict = {}

    for i in range(len(columnNames)):
      if i == 0: continue
      columnName = columnNames[i]
      avgPoint = calculateAvgPoint(listPointsString = currentStudentPoints[i])
      pointDict[columnName] = avgPoint
      # có dạng: {'Toan': 9.5}

     # lấy tên học sinh cho vào, có dạng {'1': {'Toan': 9.5}}
    studentDict[currentStudentPoints[0]] = pointDict

    listStudents.append(studentDict)
  
  # print(json.dumps(listStudents, indent=2))
  f.close()
  return listStudents

def processStudentPoint(dictPoint):
  return ";".join([str(s) for s in list(dictPoint.values())])

def luudiem_trungbinh(listDictPoints, destinationPath):
  f = open(destinationPath, "w")
  
  # Lấy ra dòng đầu tiên gồm: Ma HS, tên môn học
  columns = ", ".join(['Ma HS'] + list(listDictPoints[0]['1'].keys()))
  f.write(columns)

  # lấy ra tất cả các mã HS
  # TODO: có cách nào tốt hơn k?
  listStudentNames = []
  listStudentPoints = []
  for item in listDictPoints:
     name, point = item.popitem()
     listStudentNames.append(name)
     listStudentPoints.append(processStudentPoint(point))

  for i in range(len(listStudentNames)):
    f.write("\n")
    f.write(listStudentNames[i] + "; " + listStudentPoints[i])
  
  f.close()

def main():
    result = tinhdiem_trungbinh("./diem_chitiet.txt")
    luudiem_trungbinh(result, "./diem_trungbinh.txt")

if __name__ == "__main__":
    main()

