weight = float(input())
height = float(input())

imc = weight / (height ** 2.0)

if imc < 18.5:
    print("Underweight")
elif 25.0 > imc:
    print("Normal")
elif imc < 30.0:
    print("Overweight")
else:
    print("Obesity")
