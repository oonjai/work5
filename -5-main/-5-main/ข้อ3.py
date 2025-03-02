print("3.)เขียนโปรเเกรม Username เเละ Password เพื่อตรวจสอบว่า Admin หรือไม่ กำหนดให้")
print("          -Username คือ admin\n          -Password คือ Ad13n@23t\n--------------------------------------")
Admin_Username = "admin"
Admin_Password = "Ad13n@23t"
Username = input("Username : ")
Password = input("Password : ")
if(Admin_Username == Username and Admin_Password == Password) :
    print("Welcome, admin")
else :
    print("You are not admin")
