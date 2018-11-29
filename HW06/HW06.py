# @author:Ziyu Zhang
# HW06 for SSW 810

import unittest
from random import randint


def remove_vowels(string):
    str_list = list(string)
    for item in str_list:
        if item in ['a', 'e', 'i', 'o', 'u']:
            str_list.remove(item)

    '''
    str_list = [item for item in string if item.lower() in ['a', 'e', 'i', 'o', 'u']]
    '''
    return ''.join(str_list)


def check_pwd(pwd):
    pwd_list = list(pwd)
    bool_list = [True] * 3
    '''
    for letter in pwd_list:
        # Check each item once with and not bool_list[x]
        if letter.isupper() and bool_list[0]:
            bool_list[0] = False
        if letter.islower() and bool_list[1]:
            bool_list[1] = False
        if letter.isdigit() and bool_list[2]:
            bool_list[2] = False
    '''
    while len(pwd_list) > 0:
        letter = pwd_list.pop()
        if letter.isupper() and bool_list[0]:
            bool_list[0] = False
        if letter.islower() and bool_list[1]:
            bool_list[1] = False
        if letter.isdigit() and bool_list[2]:
            bool_list[2] = False
    return not any(bool_list)


def insertion_sort(sequnce):
    '''
    seq_list = list(sequnce)
    for i in range(1, len(seq_list)):
        tmp = seq_list[i]
        for j in range(i, 0, -1):
            # print('j: ', j)
            if seq_list[j - 1] > tmp:
                seq_list[j] = seq_list[j - 1]
                seq_list[j - 1] = tmp
                # print('for j:', seq_list)
            else:
                break
        # print(i, '[{}]'.format(seq_list[i]), seq_list)
    '''
    seq_list = list(sequnce)
    sorted_list = seq_list[:1]
    for item in seq_list[1:]:
        for value in sorted_list:
            if value > item:
                sorted_list.insert(sorted_list.index(value), item)
                # print(sorted_list)
                break
            else:
                continue
        if item >= sorted_list[len(sorted_list) - 1]:
            sorted_list.append(item)
    return sorted_list


def get_list():
    # length = int(input('length: '))
    # minimum = int(input('min: '))
    # maximum = int(input('max: '))
    num_list = []
    for i in range(0, 20):
        ran = randint(0, 40)
        num_list.append(ran)
    return num_list


class Test(unittest.TestCase):
    def test_remove_vowels(self):
        ''' Test of remove_vowels() '''
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')

    def test_check_pwd(self):
        ''' Test of checl_pwd() '''
        self.assertEqual(check_pwd('ZiyuZhang1008'), True)
        self.assertEqual(check_pwd('dsfsdf'), False)

    def test_insertion_sort(self):
        ''' Test of insertion_sort() '''
        TestList = get_list()
        sorted_list_1 = insertion_sort(TestList)
        TestList.sort()
        self.assertEqual(sorted_list_1, TestList)


def main():
    print(remove_vowels("Hello World"))
    the_list = get_list()
    print(the_list)
    print(insertion_sort(the_list))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
