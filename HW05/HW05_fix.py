# @author: Ziyu Zhang
# Homework5 for SSW 810

import unittest


def reverse(string):
    # these is only one FILO structure called stack.
    newStr = ""
    for c in string:
        newStr = c + newStr
    return newStr


def rev_enumerate(string):
    # I do not need to invoke reverse()
    for i in range(len(string) - 1, -1, -1):
        yield i, string[i]


def find_second(str1, str2):
    # This is interesting. Firstly I was considering to use a character matching algorithm \
    # But, after rethinking, I found I only have to invoke find() again.
    firstIndex = str2.find(str1)
    if firstIndex == -1:
        return -1
    else:
        length = firstIndex + len(str1)
        return str2.find(str1, length)


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open " ', path, ' ", plz check. ')
    else:
        with fp:
            lines = fp.readlines()
            i = 0
            while i < len(lines):
                # I will add i manually in some cases so I will not use 'for loops'
                line = lines[i].rstrip('\n\r')
                lineList = list(line)
                # Transfer string into list, because list can simulate stack with its method pop()
                if not lineList:
                    i += 1
                    continue
                # I do not want a emtpy sequence to show up on my final output. (This happens, think about the final line!
                # Firstly I was trying to use break, because I know it is in the end, HOWEVER, I think continue is more logical.
                # This is one disadvantage of while loop. I forget to plus i by 1 here. Sorry for carelessness.

                while '\\' == lineList[len(line) - 1]:
                    lineList.pop()
                    # '\' is at the end of each sequence, so do you remember there is an FILO structure called stack?
                    line = "".join(lineList)
                    line += lines[i + 1].rstrip('\n\r')
                    lineList = list(line)
                    i += 1
                    # This i += 1 is for I sticking next line with present line together, so I cannot read next line again.

                i += 1
                # I put the final 'i += 1' here because if I put it in the end, it might not execute. What is more, i will not be used below.

                for j in range(len(line)):
                    if '#' == line[j]:
                        j -= 1
                        # Offsets problems, think carefully with '[0: j + 1]'. I failed here mamy times.
                        break
                if j == -1:
                    # This -1 is so important.
                    continue
                else:
                    string = str(line[0: j + 1])
                    # I have to plus 1 because it is an open set.
                    yield string


class Test(unittest.TestCase):
    def test_reverse(self):
        '''Test of reverse()'''
        self.assertEqual(reverse('TheQuickBrownFoxJumpsOverTheLazyDog'), 'TheQuickBrownFoxJumpsOverTheLazyDog'[::-1])
        self.assertEqual(reverse('honorificabilitudinitatibus'), 'honorificabilitudinitatibus'[::-1])

    def test_rev_enumerate(self):
        '''Test of rev_enumerate()'''
        RevEnuList = list(rev_enumerate('abcde'))
        expect = [(4, 'e'), (3, 'd'), (2, 'c'), (1, 'b'), (0, 'a')]
        self.assertEqual(RevEnuList, expect)

    def test_find_second(self):
        '''Test of find_second()'''
        self.assertEqual(find_second('i', 'honorificabilitudinitatibus'), 7)

    def test_get_line(self):
        '''Test of get_line()'''
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        self.assertEqual(list(get_line('test.txt')), expect)


def main():
    """
    print('In main. ')
    string = '12345'
    str1 = 'abc'
    str2 = 'abcabc'
    print('Part 1: \n', reverse(string))

    print('Part 2: ')
    print(list(rev_enumerate(string)))
    for i, cha in rev_enumerate(string):
        print(i, cha)

    print('Part 3: ')
    print(find_second(str1, str2))
    """
    file_path = 'test.txt'
    print(list(get_line(file_path)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
