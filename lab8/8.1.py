import statistics

def main():
  inputString = input("Nhap chuoi chieu cao = ")
  splitedStrings = inputString.split(sep=" ")
  setHeights = { float(string) for string in splitedStrings }

  print(f"Chieu cao trung binh: { round(statistics.mean(setHeights) ,2) }")

if __name__ == '__main__':
  main()