class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.name[0] + self.last_name + self.birth_year

name2 = input()
last_name2 = input()
birth_year2 = input()

new_student = Student(name2, last_name2, birth_year2)
print(new_student.student_id)
