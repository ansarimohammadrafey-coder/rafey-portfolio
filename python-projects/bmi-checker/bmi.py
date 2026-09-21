# BMI Calculator
# Created by Rafey

print("===== BMI CALCULATOR =====")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

if weight <= 0 or height <= 0:
    print("Please enter valid values.")

else:
    bmi = weight / (height * height)

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("BMI category: Underweight")

    elif bmi < 25:
        print("BMI category: Normal range")

    elif bmi < 30:
        print("BMI category: Overweight")

    else:
        print("BMI category: Obesity")