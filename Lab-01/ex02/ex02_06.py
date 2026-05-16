input_str = input("Nhập vào X, Y: ")
dimesions=[int(x) for x in input_str.split(",")]
rowNum=dimesions[0]
colNum=dimesions[1]
multilist = [[0 for i in range(colNum)] for j in range(rowNum)]
for i in range(rowNum):
    for j in range(colNum):
        multilist[i][j]=i*j
print(multilist)