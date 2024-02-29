import datetime

class Student:

    def __init__(self, idnum, name, dob, year):
        self.id = idnum
        self.name = name
        self.dob = dob
        self.year = year

    def calc_age(self):
        today = datetime.date.today()
        year = today.year
        dob_year = self.dob[-4:]
        age = int(year) - int(dob_year)
        print(f"The student's current age is {age}")
        return age
          
    def reg_dates(self):
        if self.year == "senior" or self.year == "Senior":
            reg_date = "4/1 through 4/3"
        elif self.year == "Junior" or self.year == "junior":
            reg_date = "4/4 through 4/6"
        elif self.year == "Sophomore" or self.year == "sophomore" or self.year == "soph":
            reg_date = "4/7 through 4/9"
        elif self.year == "Freshman" or self.year == "freshman" or self.year == 'fresh' or self.year == 'frosh':
            reg_date = "4/10 through 4/12"
        else:
            print("invalid class year, please rerun program and reinput.")
        print(f"This student can register between {reg_date}")
        return reg_date