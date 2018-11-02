# @author: Ziyu Zhang
# HW09 SSW 810
import os
import unittest
from prettytable import PrettyTable
from reader import csv_reader


class Student():
    __slots__ = {"cwid", "name", "major", "course_grade"}

    def __init__(self, cwid='10442561', name="Ziyu Zhang", major="SFEN"):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course_grade = dict()

    def add_course_grade(self, cwid, course, grade):
        if cwid == self.cwid:
            self.course_grade[course] = grade

    def get_course_grade(self):
        # Actually I can visit course_grade directly due to python's character
        return self.course_grade


class Instructor():
    __slots__ = {"cwid", "name", "dept", "course_stu_num"}

    def __init__(self, cwid='00000', name="Jim Rowland", dept="SFEN"):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course_stu_num = dict()

    def add_course_stu_num(self, cwid, course):
        if cwid == self.cwid:
            self.course_stu_num.setdefault(course, 0)
            self.course_stu_num[course] += 1

    def get_course_stu_num(self):
        # So as get_course_grade
        return self.course_stu_num


class Repository():
    __slots__ = {"stu_data", "ins_data", "working_path", "course_data"}

    def __init__(self, dir_path=os.getcwd()):
        self.working_path = dir_path
        self.stu_data = dict()
        self.ins_data = dict()
        self.course_data = list()

    def read_stu(self):
        stu_dir = os.path.join(self.working_path, "students.txt")
        reader_gen = csv_reader(stu_dir, 3, '\t', False)
        for cwid, name, major in reader_gen:
            new_stu = Student(cwid=cwid, name=name, major=major)
            self.stu_data[new_stu.cwid] = new_stu
            # Store every new student into student data.dept
            # Maybe in future, we can conncet to database to finish these steps

    def read_ins(self):
        ins_dir = os.path.join(self.working_path, "instructors.txt")
        reader_gen = csv_reader(ins_dir, 3, '\t', False)
        for cwid, name, dept in reader_gen:
            new_ins = Instructor(cwid=cwid, name=name, dept=dept)
            self.ins_data[new_ins.cwid] = new_ins
            # Same as new student

    def read_grade(self):
        gd_dir = os.path.join(self.working_path, "grades.txt")
        gd_gen = csv_reader(gd_dir, 4, '\t', False)

        for cwid, course, grade, ins_id in gd_gen:
            for stu in self.stu_data.values():
                if cwid == stu.cwid:
                    stu.add_course_grade(cwid, course, grade)

            for ins in self.ins_data.values():
                if ins_id == ins.cwid:
                    ins.add_course_stu_num(ins_id, course)

            self.course_data.append({'cwid': cwid, 'course': course, 'grade': grade, 'ins_id': ins_id})

    def stu_table(self):
        field_name = ['CWID', 'Name', 'Courses']
        table = PrettyTable(field_names=field_name)

        for cwid, stu in self.stu_data.items():
            table.add_row([cwid, stu.name, list(stu.get_course_grade().keys())])
            # Focus on the container of student courses.
            # The keys are course names and values are grades.
        print(table.get_string(sortby='CWID'))

        lst = list()
        for cwid, stu in self.stu_data.items():
            lst.append((cwid, stu.name, list(stu.get_course_grade().keys())))

        return lst

    def ins_table(self):
        field_name = ['CWID', 'Name', 'Dept', 'Course', 'Students']
        table = PrettyTable(field_names=field_name)

        for cwid, ins in self.ins_data.items():
            for course, students in ins.get_course_stu_num().items():
                # Focus on the cotainer of instructors courses.
                # The keys are courses and the values are student numbers.
                table.add_row([cwid, ins.name, ins.dept, course, students])
        print(table.get_string(sortby='CWID'))

        lst = list()
        for cwid, ins in self.ins_data.items():
            for course, students in ins.get_course_stu_num().items():
                lst.append((cwid, ins.name, ins.dept, course, students))
        return lst


class TestRepository(unittest.TestCase):
    """
    Test of class Repository
    """

    def test_stu_table(self):
        # I am finding a way to invoke read_stu(), read_ins() and read_grades() automatically \
        # when invoke stu_table() or ins_table as long as no data in containers.
        test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW09\TestCase')
        test.read_stu()
        test.read_ins()
        test.read_grade()
        self.assertEquals(test.stu_table(), [('10442561', 'Ziyu, Z', ['SSW 810'])])

    def test_ins_table(self):
        test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW09\TestCase')
        test.read_stu()
        test.read_ins()
        test.read_grade()
        test.ins_table()
        self.assertEquals(test.ins_table(), [('00000', 'Rowland, J', 'SFEN', 'SSW 810', 1)])


def main():
    stevens = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW09')
    stevens.read_stu()
    stevens.read_ins()
    stevens.read_grade()
    stevens.stu_table()
    stevens.ins_table()

    test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW09\TestCase')
    test.read_stu()
    test.read_ins()
    test.read_grade()
    test.ins_table()
    test.stu_table()


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    # main()
