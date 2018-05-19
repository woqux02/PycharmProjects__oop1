class Student():
    pass
Sun = Student()

class DOstu():
    name = None
    age = 18
    course = "Python"
    def dohomework(self):
        print("我在做作业")
        return None

# 实例化类
Wei = DOstu()
Wei.name = "Sunweibo"
Wei.age = 20
print(Wei.age)
print(Wei.name)
Wei.dohomework()
