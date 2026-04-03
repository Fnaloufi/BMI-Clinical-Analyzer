# BMI Calculator
weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))
bmi=weight/(height**2)
print("your BMI is:",round(bmi,2))
if bmi<18.5:
    print("Category:underweight")
    print("Risk:Possible malnutrition")
elif bmi<25:
    print("Category:Normal weight")
    print("Risk:Low health risk")
elif bmi<30:
    print("category:overweight")
    print("Risk:Increased risk of metabolic disease")
else:
    print("category:obese")
    print("Risk:High risk of carsiovascular disease")