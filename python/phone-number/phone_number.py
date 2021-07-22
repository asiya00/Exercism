class PhoneNumber:
    def __init__(self, number):
        self.area_code = "223"
        self.number = number
        num = ""
        for i in number:
            if i.isdigit():
                num+=i
        if num[0]=='1' and '223' in num:
            num = num[1:]
            if num[3]=='0' or num[3]=='1':
                raise ValueError("Invalid Number")
            else:
                self.number = num
        elif num[0]=='0' or num[3]=='0' or num[3]=='1' or '223' not in num:
            raise ValueError("Invalid Number")
        elif len(num)<10 or len(num)>10:
            raise ValueError("Invalid Number")
        else:
            self.number = num
    
    def pretty(self):
        return "({})-{}-{}".format(self.number[0:3],self.number[3:6],self.number[6:])
