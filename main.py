class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade


class Teacher:
    def __init__(self, tid, name):
        self.tid = tid
        self.name = name
        self.subjects = []


class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student):
        self.students[student.sid] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.tid] = teacher

    def assign_grade(self, sid, subject, grade):
        if sid in self.students:
            self.students[sid].add_grade(subject, grade)
