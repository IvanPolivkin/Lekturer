class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__ (self):
        res = f'Имя: {self.name} Фамилия: {self.surname} Средння оценка за домашнее задание: {self.grades} Курсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.finished_courses}'
        return res
    
    def rate_L_M(self, lektor, lec, grade):
        if isinstance(lektor, Lekturer) and lec in self.lec:
            if lec in lektor.grades:
                lektor.grades[lec] += [grade]
            else:
                lektor.grades[lec] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        pes = f'Имя: {self.name} Фамилия: {self.surname}'
        return pes

class Lekturer (Mentor):
    def init(self, name, surname):
        super().init(name, surname)
        self.name = name
        self.surname = surname
        self.lec = []
        self.grades = {}

    def __str__(self):
        ses = f'Имя: {self.name} Фамилия: {self.surname} Средняя оценка за лекции: {self.grades}'
        return ses

class Reviewer (Mentor):      
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']  # добавление в список курсов в обучении

student_2 = Student('Pol', 'Cosinsky', 'male')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Python']

student_3 = Student('Lola', 'Kolola', 'female')
student_3.courses_in_progress += ['Python'] 
student_3.finished_courses += ['Git']

mentor_1 = Reviewer('Some', 'Buddy')
mentor_1.courses_attached += ['Python', 'Git']

lekturer_1 = Lekturer('Pierce', 'Brosnan') # добавление в список преподаваемых курсов
# lekturer_1.lec += ['Python', 'Git']

 
mentor_1.rate_hw(student_1, 'Python', 10)
mentor_1.rate_hw(student_2, 'Git', 8)
mentor_1.rate_hw(student_3, 'Python', 7)
# student_1.rate_L_M(lekturer_1, 'Python', 10)
 
print(student_1.grades)
print(student_2.grades)
print(student_3.grades)

print(student_2)
# print(lekturer_1)
print(mentor_1)
# print(student_1 > student_3)