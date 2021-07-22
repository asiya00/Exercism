def is_isogram(string):
    string = string.lower()
    string = string.replace("-","")
    string = string.replace(" ","")
    distinctchar = set(string)
    for i in distinctchar:
        if string.count(i)!= 1:
            return False
    return True
