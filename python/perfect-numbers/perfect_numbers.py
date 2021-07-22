def classify(number):
    if number>0:
        add = 0
        for i in range(1,number):
            if number%i==0:
                add += i
        if add == number:
            return "perfect"
        elif add > number:
            return "abundant"
        else:
            return "deficient"
    else:
        raise ValueError("Non negative and non zero numbers are not allowed")


