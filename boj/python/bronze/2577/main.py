A,B,C = int(input()), int(input()), int(input())
result = A * B * C
stringResult = str(result)
resultMap = {}

for i in range(len(stringResult)):
  resultMap[stringResult[i]] = resultMap.get(stringResult[i], 0) + 1

for i in range(10):
  print(resultMap.get(str(i), 0))