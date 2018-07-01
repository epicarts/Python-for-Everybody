num = 0
tot = 0.0
number = False
while True :
    sval = input('Enter a number.')
    if sval == 'done' & number is False:
        break
    try:
        fval = float(sval)
        number = True
    except:
        print('Invalid input')
        continue

    num = num + 1
    tot = tot +fval

print(tot, num, tot / num)
