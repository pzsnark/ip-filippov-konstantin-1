import sys
name = "Konstantin"
age = int(input("Введите возраст:"))
age2 = age - 18
print("Значение:", age2)
if age2 > 0:
    text2 = "старше"
elif age2 == 0:
    print("Константину 18 лет")
    sys.exit()
else:
    text2 = "младше"
age2 = abs(age2)
if age2 >= 5 and age2 <= 20:
    text = "лет"
else:
    if (age2 % 10) == 1:
        text = "год"
    elif (age2 % 10) >= 2 and (age2 % 10) <= 4:
        text = "года"
    else:
        text = "лет"
print("Константин на", abs(age2), text, text2, "18")
