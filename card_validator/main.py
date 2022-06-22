cn = input("Enter your Credit card number: ")
flg = 0
try:
    int(cn)
    if len(cn) < 16 or len(cn)>16:
        print("16 Digits Required")
    elif len(cn) == 16:
        flg = 1
except:
    print("enter only number")

if flg == 1:
    edit1 = ""
    for i in range(16):
        if i % 2 == 0:
            en = 2 * int(cn[i])

            if en > 9:
                ens = str(en)
                edit1 = edit1 + str(int(ens[0]) + int(ens[1]))
            else:
                edit1 = edit1 + (str(2*int(cn[i])))
        else:
            edit1 = edit1 + cn[i]

    sum = 0
    for i in edit1:
        sum += int(i)
    print("Valid") if str(sum)[-1] == '0' else print("not valid")
