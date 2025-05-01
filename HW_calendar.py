class Mydate:
    def __init__(self, year=1, month=1, day=1):
        self.year = year
        if self.year < 1:
            self.year = 1

        self.month = month
        if self.month > 12:
            self.month = 12
        elif self.month < 1:
            self.month = 1

        self.day = day
        if self.day < 1:
            self.day =1

        #self.day = self.day_move(self.year, self.month, day) #이해X

    def leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def month_days(self, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.leap(self.year) else 28
        
    def day_move(self,year,month,day):
        if self.leap(self.year) and month==2 and day> 29:
            day = 29
        elif year !=self.leap(self.year) and month==2 and day>28:
            day = 28
        

    # def day_move(self, year, month, day): #이해X
    #     max_day = self.month_days(month)
    #     if day > max_day:
    #         return max_day
    #     return day

    def show(self):
        print(f"{self.year}년 {self.month}월 {self.day}일")

d = Mydate(2024, 2, 30)
d.show()