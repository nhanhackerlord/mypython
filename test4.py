import sys
import time
import os
a = int(input("Nhập key tool:  "))
if a == (1711):
    print("Mật khẩu đúng")
else:
    sys.exit("Mật khẩu sai")
print("1.Xem giờ") == 1
print("2.Calculator") == 2
print("3.Spam từ") == 3
print("4.Restart máy") == 4
print("5.Xét tam giác")
x = int(input("Chọn chức năng:  "))
# Chức năng 1
if (x == 1):
    t=time.localtime(time.time())
    localtime=time.asctime(t)
    str="Bây giờ là :"+time.asctime(t)
    print (str);
#end
# Chức năng 2
if (x == 2):
    print("Bạn muốn tính phép tính nào?")
    operator = input("+ - * /: ")
    n1 = int(input("Số thứ 1: "))
    n2 = int(input("Số thứ 2: "))
    if operator == '+':
      print(n1, operator, n2, "=", n1+n2)
      
    elif operator == '-':
      print(n1, operator, n2, "=", n1-n2)

    elif operator == '*':
      print(n1, operator, n2, "=", n1*n2)

    elif operator == '/':
      print(n1, operator, n2, "=", n1/n2)

    else:
      print("Phép tính lỗi [Error]")
      print("Dấu chỉ được gồm * / + -") 
#end
if (x == 3):
    d = input("Nhập từ cần spam:  ")
    c = int(input("Nhập số lần cần spam: "))
    for i in range (c):
        print(d)
if (x == 4):
    shutdown = input("Khoi dong lai may? yes/no:       ")
    if shutdown == 'no':
        exit()
    else:
	    os.system("shutdown /s /t 1")
if (x == 5):
    i = int(input("Nhap canh a:    "))
    k = int(input("Nhap canh b:    "))
    l = int(input("Nhap canh c:    "))
    if (i + k > l and i + l > k and l + k > i and i > 0 and k > 0 and l > 0):
         print("Day la 1 tam giac")
    else:
         print("Day ko phai la 1 tam giac")