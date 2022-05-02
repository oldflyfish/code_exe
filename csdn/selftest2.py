class student(object):
    score = 91
    def get_grade(self):
        b = self.score
        print(str(b))
        if b >= 90:
            return 'A'
        elif b >= 60:
            return 'B'
        else:
            return 'C'

d = student().get_grade()