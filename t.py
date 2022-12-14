import json

dataX = open("data.txt", "r", encoding="UTF-8")
dataX = dataX.readlines()
b = []
a = []
for data in dataX:
    for dataT in json.loads("{"+data+"}").values():
        a.append(dataT)
    b += json.loads("{"+data+"}").keys()
    print(a)
for p in a:
    print(436547 in p.values())
    