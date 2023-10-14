
#BMI calculator
height=float(input("Enter height in m:"))
weight=int(input("Enter weight in kg:"))
BMI = (weight) / (height*height)


status=''
if BMI<=18.5:
    status= "Underweight"
elif BMI >18.5 or BMI <=25:
        status="Normal Weight"
elif BMI>25 or BMI <=30:
        status="Overweight"
elif BMI>30 or BMI <=35:
        status= "Obese"
elif BMI>35:
        status="Clinically Obese"
    

print("Your BMI is", round(BMI,1), "you are", status)


