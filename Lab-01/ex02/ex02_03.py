#Nhập số từ người dùng
so = int(input("Nhập một số: "))
#Kiểm tra xem số đó có phải là số chẵn hay không
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    #Không phải số chẵn
    print(f"{so} là số lẻ.")
