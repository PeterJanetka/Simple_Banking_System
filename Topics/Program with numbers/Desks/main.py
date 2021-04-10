group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

students_per_desk = 2

class_1 = (group_1 % students_per_desk) + (group_1 // students_per_desk)
class_2 = (group_2 % students_per_desk) + (group_2 // students_per_desk)
class_3 = (group_3 % students_per_desk) + (group_3 // students_per_desk)

print(int(class_1) + int(class_2) + int(class_3))
