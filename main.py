class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}
        self.students = []


#функция выставления оценки лекторам студентами
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

#перезагрузка магического метода
    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
            self.all_grades.extend(grade)
            rating = sum(self.all_grades) / len(self.all_grades)

        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' '\n' \
           f'Средняя оценка за домашнее задание: {round((rating),2)}' \
          '\n' f'Курсы с процессе изучения: {self.courses_in_progress}' '\n'\
          'Завершенные курсы: Введение в программирование'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#реализация наследования классов от Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.rating = []

# перезагрузка магического метода
    def __str__(self):
        self.all_grades = []
        for grade in self.grades.values():
             self.all_grades.extend(grade)
        rating = sum(self.all_grades) / len(self.all_grades)
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}' \
             '\n' f'Средняя оценка за лекции: {round((rating),2)}'

#метод для сравнений
    def __lt__(self,other):
         self.all_grades = []
         for grade in self.grades.values():
            self.all_grades.extend(grade)
         rating = int(sum(self.all_grades) / len(self.all_grades))
         return self.rating > other.rating

#реализация наследования классов от Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# Возможность выставлять студентам оценки за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f'Имя: {self.name}'  '\n' f'Фамилия: {self.surname}'



#экземпляры классов. Полевые испытания


one_student = Student('Ruoy', 'Eman')
one_student.courses_in_progress += ['Python']
one_student.courses_in_progress += ['GIT']

another_student = Student('Eman', 'Ruoy')
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['GIT']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']
cool_Reviewer.courses_attached += ['GIT']

one_Reviewer = Reviewer('Buddy', 'Some')
one_Reviewer.courses_attached += ['Python']
one_Reviewer.courses_attached += ['GIT']

cool_Reviewer.rate_hw(one_student, 'Python', 8)
cool_Reviewer.rate_hw(one_student, 'GIT', 5)

cool_Reviewer.rate_hw(one_student, 'Python', 3)
cool_Reviewer.rate_hw(one_student, 'GIT', 6)

one_Reviewer.rate_hw(one_student, 'Python', 7)
one_Reviewer.rate_hw(one_student, 'GIT', 4)

one_Reviewer.rate_hw(another_student, 'GIT', 5)
one_Reviewer.rate_hw(another_student, 'Python', 5)

cool_Lecturer = Lecturer('Buddysome', 'Somebuddy')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['GIT']

another_Lecturer = Lecturer('Anton', 'Kartoshkin')
another_Lecturer.courses_attached += ['Python']
another_Lecturer.courses_attached += ['GIT']

one_student.rate_lecturer(cool_Lecturer, 'Python', 7)
one_student.rate_lecturer(cool_Lecturer, 'GIT', 6)

one_student.rate_lecturer(another_Lecturer, 'Python', 3)
one_student.rate_lecturer(another_Lecturer, 'GIT', 7)

another_student.rate_lecturer(cool_Lecturer, 'Python', 5)
another_student.rate_lecturer(cool_Lecturer, 'GIT', 6)

another_student.rate_lecturer(another_Lecturer, 'Python', 4)
another_student.rate_lecturer(another_Lecturer, 'GIT', 8)


students_list = []
students_list.append(one_student.grades)
students_list.append(another_student.grades)

def average_student(student):
    all_points = []
    all_points_2 = []
    for course in student.grades.values():
        all_points.extend(student.grades.values())
        for grade in all_points:
            all_points_2.extend(grade)
            rating = sum(all_points_2)/len(all_points_2)
    return rating

#метод для сравнений

def __lt__(one_student, another_student):
    return average_student(one_student)< average_student(another_student)
print(average_student(one_student)> average_student(another_student))


Lecturers_list = []
Lecturers_list.append(cool_Lecturer.grades)
Lecturers_list.append(another_Lecturer.grades)

def average_Lect(courses):
    average_point = 0
    Lecturers_2 = []
    for dict in Lecturers_list:
        average_point =sum(dict[courses])/len(dict[courses])
        Lecturers_2.append(average_point)
    return sum(Lecturers_2)/len(Lecturers_2)

#метод для сравнений
def __lt__(cool_Lecturer, another_Lecturer):
    return average_student(cool_Lecturer)< average_student(another_Lecturer)
print(average_student(cool_Lecturer)> average_student(another_Lecturer))

#средняя оценка
def average_hw_grades_by_course(students_list, course_name):
    grades_list = []
    counter = 0
    for stud in students_list:
        grades_list.extend(stud[course_name])
    return sum(grades_list)/len(grades_list)

print(average_hw_grades_by_course(students_list,'Python'))

#средняя оценка
def average_hw_grades_by_course(Lecturers_list, course_name):
    grades_list = []

    for el in Lecturers_list:
        grades_list.extend(el[course_name])
    return sum(grades_list)/len(grades_list)

print(average_hw_grades_by_course(Lecturers_list,'Python'))


print(cool_Reviewer)
print(cool_Lecturer)
print(another_Lecturer)
print(one_Reviewer)
print(one_student)
print(another_student)
