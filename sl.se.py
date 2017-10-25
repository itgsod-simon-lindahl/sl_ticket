def fares(age, disscount=False, student=False, senior=False):
    if age >=20 and age < 65:
        disscount = False
    elif age >= 65 or age < 20:
        disscount = True
    if disscount or student or senior:
        return "halv"
    else:
        return "hel"

print fares(10)
print fares(65)
print fares(25, student=True)
