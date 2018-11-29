# @author: Ziyu Zhang
# HW09 SSW 810
import os
import unittest
from collections import defaultdict
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


class Major():
    __slots__ = {"major", "required", "elective"}

    def __init__(self, major):
        self.major = major
        self.required = set()
        self.elective = set()

    def add_required(self, course):
        self.required = self.required.union(set(course))

    def add_elective(self, course):
        self.elective = self.elective.union(set(course))


class Repository():
    __slots__ = {"stu_data", "ins_data", "working_path", "course_data", "major_data"}

    def __init__(self, dir_path=os.getcwd()):
        self.working_path = dir_path
        self.stu_data = dict()
        self.ins_data = dict()
        self.course_data = list()
        self.major_data = dict()

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

    def read_major(self):
        mj_dir = os.path.join(self.working_path, "majors.txt")
        reader_gen = csv_reader(mj_dir, 3, '\t', False)
        tmp_dic = defaultdict(lambda: defaultdict(set))
        for dept, flag, course in reader_gen:
            tmp_dic[dept][flag].add(course)

        for dept, courses in tmp_dic.items():
            new_major = Major(major=dept)
            for flag, course in courses.items():
                if flag == 'R':
                    new_major.add_required(course)
                if flag == 'E':
                    new_major.add_elective(course)
            self.major_data[dept] = new_major

    def major_table(self):
        field_name = ['Dept', 'Required', 'Elective']
        table = PrettyTable(field_names=field_name)
        for dept, major in self.major_data.items():
            table.add_row([dept, major.required, major.elective])
        print(table)

        lst = list()
        for dept, major in self.major_data.items():
            lst.append([dept, major.required, major.elective])
        return lst

    def stu_table(self):
        field_name = ['CWID', 'Name', 'Completed Courses', 'Required', 'Elective']
        table = PrettyTable(field_names=field_name)
        for cwid, stu in self.stu_data.items():
            remain_require = self.major_data[stu.major].required.difference(stu.get_course_grade().keys())
            remain_elective = self.major_data[stu.major].elective.intersection(stu.get_course_grade().keys())
            if len(remain_elective) == 0:
                remain_elective = self.major_data[stu.major].elective
            else:
                remain_elective = None
            table.add_row([cwid, stu.name, list(stu.get_course_grade().keys()), remain_require, remain_elective])
            # Focus on the container of student courses.
            # The keys are course names and values are grades.
        print(table.get_string(sortby='CWID'))

        lst = list()
        for cwid, stu in self.stu_data.items():
            lst.append((cwid, stu.name, list(stu.get_course_grade().keys()), remain_require, remain_elective))

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

    def test_major_table(self):
        test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW10\TestCase')
        test.read_stu()
        test.read_ins()
        test.read_grade()
        test.read_major()
        self.assertEquals(test.major_table(), [['SFEN', {'SSW 567', 'SSW 564', 'SSW 540', 'SSW 555'}, {'CS 501', 'CS 545', 'CS 513'}]])

    def test_stu_table(self):
        # I am finding a way to invoke read_stu(), read_ins() and read_grades() automatically \
        # when invoke stu_table() or ins_table as long as no data in containers.
        test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW10\TestCase')
        test.read_stu()
        test.read_ins()
        test.read_grade()
        test.read_major()
        self.assertEquals(test.stu_table(), [('10442561', 'Ziyu, Z', ['SSW 810'], {'SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'}, {'CS 545', 'CS 501', 'CS 513'})])

    def test_ins_table(self):
        test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW10\TestCase')
        test.read_stu()
        test.read_ins()
        test.read_grade()
        test.read_major()
        self.assertEquals(test.ins_table(), [('00000', 'Rowland, J', 'SFEN', 'SSW 810', 1)])


def main():
    stevens = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW10')
    stevens.read_stu()
    stevens.read_ins()
    stevens.read_grade()
    stevens.read_major()
    stevens.major_table()
    stevens.stu_table()
    stevens.ins_table()

    test = Repository(dir_path=r'C:\Users\64937\OneDrive\Documents\SSW\810\HW10\TestCase')

    test.read_stu()
    test.read_ins()
    test.read_grade()
    test.read_major()
    test.ins_table()
    print(test.stu_table())
    print(test.major_table())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
