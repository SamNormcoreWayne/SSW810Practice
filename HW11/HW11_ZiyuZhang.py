import pymysql


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open {}'.format(path))
    else:
        with fp:
            for line in fp:
                yield line


def csv_reader(path, fields, sep=',', header=False):
    for line in list(get_line(path)):
        line = line.rstrip('\n')
        # print(line)
        lst = line.split(sep)
        if header is True:
            if len(lst) != fields:
                raise ValueError('Expected {} fields, but the header only has {}.'.format(fields, len(lst)))
            header = False
            continue
        # print(lst)
        if len(lst) != fields:
            raise ValueError('Expected {} fields, but it is {}.'.format(fields, len(lst)))
        yield tuple(lst)


def main():
    db = pymysql.connect("localhost", "root", "123456", "sswrepository_zzy")
    cursor = db.cursor()
    grades = list(csv_reader(r'C:\Users\64937\OneDrive\Documents\SSW\810\HW11\HW11_grades.txt', 4, '\t', True))
    for line in grades:
        try:
            cursor.execute("INSERT INTO grades (stu_CWID, course, grade, ins_CWID) VALUES ('{}', '{}', '{}', '{}');".format(line[0], line[1], line[2], line[3]))
            db.commit()
        except pymysql.err.InternalError:
            db.rollback()
    ins = list(csv_reader(r'C:\Users\64937\OneDrive\Documents\SSW\810\HW11\HW11_instructors.txt', 3, '\t', True))
    for line in ins:
        try:
            cursor.execute("INSERT INTO instructors (CWID, Name, Dept) VALUES ('{}', '{}', '{}');".format(line[0], line[1], line[2]))
            db.commit()
        except pymysql.err.InternalError:
            db.rollback()

    stu = list(csv_reader(r'C:\Users\64937\OneDrive\Documents\SSW\810\HW11\HW11_students.txt', 3, '\t', True))
    for line in stu:
        try:
            cursor.execute("INSERT INTO students (CWID, Name, Major) VALUES ('{}', '{}', '{}');".format(line[0], line[1], line[2]))
            db.commit()
        except pymysql.err.InternalError:
            db.rollback()

    major = list(csv_reader(r'C:\Users\64937\OneDrive\Documents\SSW\810\HW11\HW11_majors.txt', 2, '\t', True))
    for line in major:
        try:
            cursor.execute("INSERT INTO majors (Major, Course) VALUES ('{}', '{}');".format(line[0], line[1]))
            db.commit()
        except pymysql.err.InternalError:
            db.rollback()


if __name__ == '__main__':
    main()
