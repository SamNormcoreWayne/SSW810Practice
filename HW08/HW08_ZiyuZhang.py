import datetime
import os
import operator
import unittest
from collections import defaultdict
from prettytable import PrettyTable

"""
All '#' are testing I wrote while debugging
All ''' ''' are docstrings FYI
"""


def date_arithmetic():
    '''
    this is easy
    '''
    date1 = "Feb 27, 2000"
    date2 = "Feb 27, 2017"
    date3 = "Jan 1, 2017"
    date4 = "Oct 31, 2017"
    dt1 = datetime.datetime.strptime(date1, '%b %d, %Y')
    dt2 = datetime.datetime.strptime(date2, '%b %d, %Y')
    dt3 = datetime.datetime.strptime(date3, '%b %d, %Y')
    dt4 = datetime.datetime.strptime(date4, '%b %d, %Y')
    num_days = 3
    print((dt1 + datetime.timedelta(days=num_days)).strftime('%d %b %y'))
    print((dt2 + datetime.timedelta(days=num_days)).strftime('%d %b %y'))
    print((dt4 - dt3).days)


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open {}'.format(path))
    else:
        with fp:
            for line in fp:
                yield line
                '''
                Firstly, I used line.strip(' ').
                then I found it would not count blankspaces or blank lines in my scanning_dir_file():(
                So I delete it.
                '''


def csv_reader(path, fields, sep=',', header=False):
    for line in list(get_line(path)):
        line = line.rstrip('\n')
        if header is True:
            if len(header) != fields:
                raise ValueError('Expected {} fields, but the header only has {}.'.format(fields, len(header)))
            header = False
            continue
        # print(line)
        lst = line.split(sep)
        # print(lst)
        if len(lst) != fields:
            raise ValueError('Expected {} fields, but it is {}.'.format(fields, len(lst)))
        yield tuple(lst)


class TestCSVReader(unittest.TestCase):
    def test_csv_reader(self):
        for one, two, three, four in csv_reader('test.csv', 4, sep=',', header=False):
            self.assertEqual((one, two, three, four), ('A1', 'B1', 'C1', 'D1'))


def scanning_dir_file(directory):
    detail_counter = defaultdict(lambda: defaultdict(int))
    file_list = os.listdir(directory)
    # print(file_list)
    os.chdir(directory)
    # print(os.getcwd())
    for name in file_list:
        if name is None:
            break

        if name[-2:] == 'py':
            detail_counter[name]['File Name'] = os.path.join(directory, name)
            detail_counter[name]['Classes']
            detail_counter[name]['Functions']
            detail_counter[name]['Lines']
            detail_counter[name]['Characters']
            '''
            Intitializing default dictionary.
            I am not sure whether they are necessary.
            '''

            for line in get_line(name):
                detail_counter[name]['Lines'] += 1
                detail_counter[name]['Characters'] += len(line)
                '''
                It seems like you are counting every character including '\n' and ' ' in your test cases,
                which makes me feel annoying.
                Because, you see, I cannot simply delete them while reading lines.
                '''
                line = line.strip()
                '''
                Sure, I delete them here.
                '''
                if 'class ' in line[:6]:
                    detail_counter[name]['Classes'] += 1
                if 'def ' in line[:4]:
                    detail_counter[name]['Functions'] += 1
    # print('1{}'.format(detail_counter.values()))

    fild_name = operator.itemgetter(0)(tuple(detail_counter.values()))
    '''
    This line is for getting title of every column, I do not want to type them AGAIN!!
    '''
    # print('2{}'.format(fild_name.keys()))

    table = PrettyTable(field_names=list(fild_name.keys()))
    for name in detail_counter:
        # print('3{}'.format(tuple(detail_counter[name].items())))
        # print('4{}'.format(tuple(detail_counter[name])))
        table.add_row(list(detail_counter[name].values()))
    print(table.get_string(sortby='Characters'))
    '''
    This sort is for sorting items by the number of lines.
    '''
    lst_file = list()
    for name in detail_counter:
        lst = list(detail_counter[name].values())
        lst[0] = name
        lst_file.append(tuple(lst))
    return set(lst_file)


def main():
    dic = r'C:\Users\64937\OneDrive\Documents\SSW\810\HW06'
    date_arithmetic()
    try:
        print(list(csv_reader('test.csv', 4, sep=',', header=False)))
    except ValueError as v:
        print(v)
    print(scanning_dir_file(dic))


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    main()
