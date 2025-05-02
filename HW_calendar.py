class Mydate:
    def __init__(self, year=1, month=1, day=1): #기본값 1년 1월 1일 
        self.year = int(year) #1보다 작은 정수이면 1년으로 셋팅
        if self.year < 1:
            self.year = 1
            
        self.month = int(month) #12보다 큰 정수 이면 12월로 셋팅, 1보다 작은 정수이면 1월로 셋팅
        if self.month > 12:
            self.month = 12
        elif self.month < 1:
            self.month = 1
            
        self.day = int(day) #1보다 작은 정수이면 1일로 셋팅
        if self.day < 1:
            self.day =1
        
        self.adjust_day() #날짜 조정 함수 호출

    def leap(self, year): #윤년 구하기
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def month_days(self, month): 
        if self.month in [1, 3, 5, 7, 8, 10, 12]: #1,3,5,7,8,10,12월은 31일 까지
            return 31
        elif self.month in [4, 6, 9, 11]: #4,6,9,11월은 30일까지 
            return 30
        elif self.month == 2: #2월에 평년에는 28까지, 윤년에는 29일
            return 29 if self.leap(self.year) else 28
        
    # 처음 만든 코드
    # def day_move(self,year,month,day): 
    #     if self.leap(self.year) and month==2 and day> 29: 
    #         day = 29
    #     elif year !=self.leap(self.year) and month==2 and day>28:
    #         day = 28
            
    def adjust_day(self): #년,월에 따라 마지막 날보다 높은 숫자를 입력하면 마지막 날 호출
        max_day = self.month_days(self.month)
        if self.day > max_day:
            self.day = max_day

    def show(self):
        print(f"{self.year}년 {self.month}월 {self.day}일")

d1 = Mydate(2024, 2, 30)
d2 = Mydate(2025, 2, 30)
d3 = Mydate(4, 1, 45)
d4 = Mydate()
d1.show()
d2.show()
d3.show()
d4.show()