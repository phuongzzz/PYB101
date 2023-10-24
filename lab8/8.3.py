stringInput = input("Nhap chuoi so = ")
removeInput = input("Nhap chuoi remove = ")

extractedNumbers = [ int(i) for i in removeInput.split(" ") if i.isdigit() ]
listNumbers = [ int(i) for i in stringInput.split(" ") ]

for removingNumber in extractedNumbers:
  if removingNumber in listNumbers:
    listNumbers.remove(removingNumber)

print(f"listNumbers: { listNumbers }")

sum = 0
for n in listNumbers:
  sum += n

print(f"result: { sum }")

