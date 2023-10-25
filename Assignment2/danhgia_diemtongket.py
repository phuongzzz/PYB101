import json

def readDataFromPath(filePath):
  # can lay duoc diem toan, ly, hoa,... cua 1 hoc sinh bat ki
  f = open(filePath, "r")

  # Doc cac cot diem
  columnNames = f.readline().replace("\n", "").replace(" ", "").split(",")

  listStudents = []
  lines = f.readlines()

  # Phan tu dau tien cua line la ma hoc sinh -> bo
  # Cac phan tu sau do la diem toan, ly, hoa, ung theo columnNames o tren
  for line in lines:
    currentStudentPoints = line.replace("\n", "").replace(" ", "").split(";")
    studentDict = {}
    pointDict = {}
    
    for i in range(len(columnNames)):
      if i == 0: continue
      columnName = columnNames[i]
      avgPoint = currentStudentPoints[i]
      pointDict[columnName] = float(avgPoint)

     # lấy tên học sinh cho vào, có dạng {'1': {'Toan': 9.5}}
    studentDict[currentStudentPoints[0]] = pointDict

    listStudents.append(studentDict)

  return listStudents

def calculatePoint(dictPoint):
  diemToan = dictPoint['Toan']
  diemLy = dictPoint['Ly']
  diemHoa = dictPoint['Hoa']
  diemSinh = dictPoint['Sinh']
  diemAnh = dictPoint['Anh']
  diemVan = dictPoint['Van']
  diemSu = dictPoint['Su']
  diemDia = dictPoint['Dia']
  
  dtb_chuan = ((diemToan + diemVan + diemAnh) * 2.0 + (diemLy + diemHoa + diemSinh + diemSu + diemDia) * 1.0) / 11.0

  maHS = ""
  listPoints = list(dictPoint.values())
  if (min(listPoints) >= 8.0) and dtb_chuan > 9.0:
    maHS = "Xuat sac"
  elif(min(listPoints) >= 6.5) and dtb_chuan > 8.0:
    maHS = "Gioi" 
  elif(min(listPoints) >= 5.0) and dtb_chuan > 6.5:
    maHS = "Kha"
  elif(min(listPoints) >= 4.5) and dtb_chuan > 6.0:
    maHS = "TB Kha"
  else:
    maHS = "TB"
  
  return maHS

def danhGiaDiemKhoiTuNhien(diem):
  if diem >= 24: return 1
  elif diem >= 18 and diem < 24: return 2
  elif diem >= 12 and diem < 18: return 3
  else: return 4

def danhGiaDiemKhoiXaHoi(diem):
  if diem >= 21: return 1
  elif diem >= 15 and diem < 21: return 2
  elif diem >= 12 and diem < 15: return 3
  else: return 4

def danhGiaDiemKhoiCoban(diem):
  if diem >= 32: return 1
  elif diem >= 24 and diem < 32: return 2
  elif diem >= 20 and diem < 24: return 3
  else: return 4

def rankingUniversity(dictPoint):
  diemToan = dictPoint['Toan']
  diemLy = dictPoint['Ly']
  diemHoa = dictPoint['Hoa']
  diemSinh = dictPoint['Sinh']
  diemAnh = dictPoint['Anh']
  diemVan = dictPoint['Van']
  diemSu = dictPoint['Su']
  diemDia = dictPoint['Dia'] 

  diemKhoiA = diemToan + diemLy + diemHoa
  diemKhoiA1 = diemToan + diemLy + diemAnh
  diemKhoiB = diemToan + diemHoa + diemSinh
  diemKhoiC = diemVan + diemSu + diemDia
  diemKhoiD = diemToan + diemVan + diemAnh * 2

  return [danhGiaDiemKhoiTuNhien(diemKhoiA), 
          danhGiaDiemKhoiTuNhien(diemKhoiA1), 
          danhGiaDiemKhoiTuNhien(diemKhoiB), 
          danhGiaDiemKhoiXaHoi(diemKhoiC), 
          danhGiaDiemKhoiCoban(diemKhoiD)]

def xeploai_hocsinh(filePath):
  listStudents = readDataFromPath(filePath)

  listStudentRanks = []
  for student in listStudents:
    studentDict = {}
    name, value = student.popitem()
    maHS = calculatePoint(value)
    studentDict[name] = maHS
    listStudentRanks.append(studentDict)

  # print(json.dumps(listStudentRanks, indent=2))
  return listStudentRanks

def xeploai_thidaihoc_hocsinh(filePath):
  listStudents = readDataFromPath(filePath)

  listStudentRanks = []

  for student in listStudents:
    studentDict = {}
    name, value = student.popitem()
    danhGiaDiemDH = rankingUniversity(value)
    studentDict[name] = danhGiaDiemDH
    listStudentRanks.append(studentDict)

  return listStudentRanks

def writeToFile(dictRanking, dictUniversityRanking):
  f = open("danhgia_hocsinh.txt", "w")
  firstRow = ",".join(["Ma HS", "xeploai_TB chuan", "xeploai_A", "xeploai_A1", "xeploai_B", "xeploai_C", "xeploai_D"])
  f.write(firstRow)

  # lay ra danh sach xep loai cua tung hoc sinh
  # sau do se merge danh sach nay voi danh sach xep loai dai hoc o duoi 
  listRanking = []
  for item in dictRanking:
    name, value = item.popitem()
    listRanking.append(value)
    
  # tao danh sach chua ket qua cuoi cung
  listResults = []

  # get all names for looping
  listNames = []
  for i in range(len(dictUniversityRanking)):
    item = dictUniversityRanking[i]
    rankingItem = listRanking[i]
    name, value = item.popitem()

    listNames.append(name)

    value = [str(s) for s in value] 
    value.insert(0, rankingItem)
    dictResult = { name: value }
    listResults.append(dictResult)
           
  for item in listResults:
    name, value = item.popitem()
    s = name + ";" + ';'.join([word for word in value])
    f.write("\n")
    f.write(s)

  f.close()

def main():
  dictRanking = xeploai_hocsinh("./diem_trungbinh.txt")
  dictUniversityRanking = xeploai_thidaihoc_hocsinh("./diem_trungbinh.txt")

  writeToFile(dictRanking, dictUniversityRanking)

if __name__ == "__main__":
    main()