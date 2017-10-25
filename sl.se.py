def fares(age, disscount=False, student=False, senior=False):
    if age >=20 and age < 65:
        disscount = False
    elif age >= 65 or age < 20:
        disscount = True
    if disscount or student or senior:
        print "halv"
        return "halv"
    else:
        print "hel"
        return "hel"

fares(10)
fares(65)
fares(25, student=True)
