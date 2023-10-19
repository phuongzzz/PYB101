class Student:
    def __init__(self, name, diemToan, diemLy, diemHoa):
        self.name = name
        self.diemToan = diemToan
        self.diemLy = diemLy
        self.diemHoa = diemHoa
        
    def print_diemtk(self):
      avg = (diemToan + diemLy + diemHoa) / 3
      print(f"The average mark of {self.name} is { round(avg, 2) }")
    

name = input()
diemToan = int(input())
diemLy = int(input())
diemHoa = int(input())

s = Student(name, diemToan, diemLy, diemHoa)
s.print_diemtk()