n = input("Nhap chuoi cac QG = ")
a = set()

countries = n.split(" ")
for c in countries:
  a.add(c)

print(f"Number of countries: {len(a)}")