class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day

    def leap(self):
        return (self.y % 4 == 0 and self.y % 100 != 0) or (self.y % 400 == 0)

    def days(self):
        a = [31,28,31,30,31,30,31,31,30,31,30,31]
        if self.leap():
            a[1] = 29
        t = 0
        for i in range(self.m - 1):
            t += a[i]
        return t + self.d

    def days_left(self):
        return (366 if self.leap() else 365) - self.days()

    def week(self):
        y, m, d = self.y, self.m, self.d
        if m < 3:
            m += 12
            y -= 1
        k = y % 100
        j = y // 100
        return (d + (13*(m+1))//5 + k + k//4 + j//4 + 5*j) % 7

    def week_name(self):
        a = ["토요일","일요일","월요일","화요일","수요일","목요일","금요일"]
        return a[self.week()]


while True:
    year, month, day = map(int, input().split())
    s = SayDays(year, month, day)
    print(s.days(), s.days_left(), s.week(), s.week_name())