print("4.) โปรเเกรมคำนวณค่า BMI\n  ซึ่ง Weight มีหน่วยเป็น Kg เเละ Height มีหน่วยเป็น m\n  BMI ที่ได้นั้นเป็นเช่นไรเทียบกับเกณฑ์ดังนี้")
print("     -Underweight เมื่อ BMI น้อยกว่า 18.5\n     -Normal weight เมื่อ BMI มีค่าตั้งเเต่ 18.5 เเต่ไม่ถึง 25\n     -Overweight เมื่อค่า BMI มีค่าตั้งเเต่ 25 เเต่ไม่ถึง 30\n     -Obesity เมื่อ BMI มีค่าไม่ตํ่ากว่า 30")
print("--------------------------------------")
W = float(input("กรุณากรอกนํ้าหนัก Weight(kg) : "))
H = float(input("กรุณากรอกส่วนสูง Height(m) : "))
BMI = W/H**2
print("--------------------------------------")
print("BMI is ", '%.2f' %(BMI))
if(BMI < 18.5) :
    print("Underweight")
elif(18.5<=BMI<25) :
    print("Normal weight")
elif(25<=BMI<30) :
    print("Overweight")
else :
    print("Obesity")
