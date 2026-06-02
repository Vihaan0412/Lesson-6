Height=float(input("Enter your height in cm:  "))
Weight=float(input("Enter your weight in kg:  "))

BMI= Weight / (Height/100)**2
print("Your BMI is",BMI)

if BMI <= 18:
    print("You are underweight")

elif  BMI <= 25:
    print("You are healty")

elif  BMI <= 30:
    print("You are overweight")


elif BMI <= 35:
    print("You are severely overweight")


elif BMI <= 40:
    print("You are obese")

else:
    print("You are severely obese")
