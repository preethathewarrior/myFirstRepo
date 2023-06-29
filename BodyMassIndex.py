w=float(input("Enter your weight in(kg):"))
h=float(input("Enter your height in(m):"))
BMI=w/h**2
print("Your BMI is:",BMI)
if 1<=BMI<18.5:
    print('You are in the "underweight" range')
elif 18.5<=BMI<25:
    print('You are in the "normal" range')
elif 25<=BMI<30:
    print('You are in the "overweight" range')
else:
    print('You are in the "Obese" range')
