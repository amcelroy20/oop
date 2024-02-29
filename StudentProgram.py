import StudentClass as s

def main():
    idnum = input('what is the id number?')
    name = input('what is the name?')
    dob = input('what is the date of birth? (mm/dd/yyyy)')
    year = input('what is the student class year?')

    newstudent = s.Student(idnum, name, dob, year)

    newstudent.calc_age()

    newstudent.reg_dates()

main()