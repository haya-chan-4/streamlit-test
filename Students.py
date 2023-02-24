class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def calc_avg(self):
        sump = sum(self.score)
        lenp = len(self.score)
        avgp = sump/lenp
        return avgp

    def is_passing_test(self):
        avg = self.calc_avg()
        if avg >= 80:
            return 'pass!'
        else:
            return 'fail!'


student1 = Student('Take', [80, 70, 70, 100, 80])
print(student1.name)
print(student1.is_passing_test())
print(student1.calc_avg())
