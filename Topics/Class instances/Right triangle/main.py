class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = (self.a * self.b) / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
my_triangle = RightTriangle(input_c, input_b, input_a)
if (input_c ** 2) == (input_a ** 2) + (input_b ** 2):
    print(my_triangle.area)
else:
    print("Not right")
