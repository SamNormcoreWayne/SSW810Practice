# @author: Ziyu Zhang
# First part of HW04
# I was trying to use 'if (i = next(gen)):', but it seems like python does not support this.
import unittest


def strGen(string):
    yield from string.lower()


def count_vowels(string):
    # Actually I came up with 3 ideas of how to implement this function.
    # The simplest one needs 'if (i = next(gen)):', but emmm as I mentioned in line 3...
    '''
    Second solution:
        for i in range(len(string)):
            if string[i] in 'aeiou':
                counter += 1
    '''
    gen = strGen(string)
    counter = 0
    for i in range(len(string)):
        if next(gen) in 'aeiou':
            counter += 1
    return counter


class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        ''' A test of count_vowels() '''
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels('honorificabilitudinitatibus'), 13)


def main():
    print("in main()")
    string = 'hello world'
    print(count_vowels(string))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
