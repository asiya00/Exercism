def is_valid(isbn):
    sum = 0
    count = 10
    isbn = isbn.replace("-","")
    if len(isbn) == 10 and (isbn[-1].isnumeric() == True or isbn[-1] == 'X'):
        isbn = isbn
    else:
        return False

    for i in isbn:
        if i.isnumeric():
            sum += int(i)*count
            count -= 1
    if isbn[-1] == 'X':
        return True if sum % 11 == 1 else False
    else:
        return True if sum % 11 == 0 else False
