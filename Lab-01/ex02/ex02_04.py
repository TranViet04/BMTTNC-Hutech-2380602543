#Tạo một danh sách rỗng để lưu kết quả
j = []
#Duyệt qua các số từ 2000 - 3200, kiểm tra nếu số đó chia hết cho 7 nhưng không phải bội số của 5
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
#In kết quả 
print(','.join(j))
