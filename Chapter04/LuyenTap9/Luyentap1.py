def bmi(weight: float, height: float) -> float:
    return round(weight / (height * height), 2)
w = float(input("Enter weight in kg: "))
h = float(input("Enter height in m: "))
print("BMI =", bmi(w, h))
